import struct
from .nbfx import Nbfx
from kaitaistruct import KaitaiStream, KaitaiStruct, ConsistencyError, EndOfStreamError
from io import BytesIO

__all__ = [
    "nbfx_export_values",
    "nbfx_import_values",
    "nbfx_serialize",
    "nbfx_get_multibyte_int31",
    "Nbfx",
]


class OldMultiByteInt31(object):
    def __init__(self, *args):
        self.value = args[0] if len(args) else None

    def to_bytes(self):
        """
        >>> MultiByteInt31(268435456).to_bytes()
        b'\\x80\\x80\\x80\\x80\\x01'
        >>> MultiByteInt31(0x7f).to_bytes()
        b'\\x7f'
        >>> MultiByteInt31(0x3fff).to_bytes()
        b'\\xff\\x7f'
        >>> MultiByteInt31(0x1fffff).to_bytes()
        b'\\xff\\xff\\x7f'
        >>> MultiByteInt31(0xfffffff).to_bytes()
        b'\\xff\\xff\\xff\\x7f'
        >>> MultiByteInt31(0x3fffffff).to_bytes()
        b'\\xff\\xff\\xff\\xff\\x03'
        """
        value_a = self.value & 0x7F
        value_b = (self.value >> 7) & 0x7F
        value_c = (self.value >> 14) & 0x7F
        value_d = (self.value >> 21) & 0x7F
        value_e = (self.value >> 28) & 0x03
        if value_e != 0:
            ret = struct.pack(
                b"<BBBBB",
                value_a | 0x80,
                value_b | 0x80,
                value_c | 0x80,
                value_d | 0x80,
                value_e,
            )
        elif value_d != 0:
            ret = struct.pack(
                b"<BBBB", value_a | 0x80, value_b | 0x80, value_c | 0x80, value_d
            )
        elif value_c != 0:
            ret = struct.pack(b"<BBB", value_a | 0x80, value_b | 0x80, value_c)
        elif value_b != 0:
            ret = struct.pack(b"<BB", value_a | 0x80, value_b)
        else:
            ret = struct.pack(b"<B", value_a)
        return bytes(ret)

    def __str__(self):
        return str(self.value)

    @classmethod
    def parse(cls, fp):
        """
        >>> from io import BytesIO
        >>> fp = BytesIO(b'\\x7f')
        >>> mb = MultiByteInt31.parse(fp)
        >>> mb.value
        127
        >>> fp = BytesIO(b'\\xff\\x7f')
        >>> mb = MultiByteInt31.parse(fp)
        >>> mb.value
        16383
        >>> fp = BytesIO(b'\\xb9\\x0a')
        >>> mb = MultiByteInt31.parse(fp)
        >>> mb.value
        1337
        """
        v = 0
        # tmp = ''
        for pos in range(4):
            b = fp.read(1)
            # tmp += b
            value = struct.unpack(b"<B", b)[0]
            v |= (value & 0x7F) << 7 * pos
            if not value & 0x80:
                break
        # print ('%s => 0x%X' % (repr(tmp), v))

        return cls(v)


def nbfx_export_values(nbfx: Nbfx) -> dict:
    ret = {"Dictionary": [], "NbfxString": [], "Number": [], "Chars": []}
    for i, entry in enumerate(nbfx.dictionary_table.entries.entry):
        ret["Dictionary"].append((i, entry.str))
    for i, record in enumerate(nbfx.records):
        try:
            rec = record.rec_body
            if isinstance(rec, Nbfx.PrefixAttribute):
                ret["NbfxString"].append((i, "name", rec.name.str))
                ret["NbfxString"].append((i, "value", rec.value.str))
            elif isinstance(rec, Nbfx.DictionaryAttribute):
                ret["NbfxString"].append((i, "prefix", rec.prefix.str))
            elif (
                isinstance(rec, Nbfx.Chars8Text)
                or isinstance(rec, Nbfx.Chars16Text)
                or isinstance(rec, Nbfx.Chars32Text)
            ):
                ret["Chars"].append((i, rec.string))
            elif (
                isinstance(rec, Nbfx.Int8Text)
                or isinstance(rec, Nbfx.Int16Text)
                or isinstance(rec, Nbfx.Int32Text)
                or isinstance(rec, Nbfx.DoubleText)
                or isinstance(rec, Nbfx.FloatText)
            ):
                ret["Number"].append((i, rec.value))
        except AttributeError:
            pass
    return ret


def nbfx_import_values(nbfx: Nbfx, values) -> Nbfx:
    for val in values["Dictionary"]:
        nbfx_str = nbfx.dictionary_table.entries.entry[val[0]]
        nbfx_set_string(nbfx_str, val[1])
        nbfx.dictionary_table.entries.entry[val[0]] = nbfx_str
    dict_len = len(kaitai_serialize(nbfx.dictionary_table.entries))
    nbfx.dictionary_table.size = nbfx_get_multibyte_int31(dict_len)

    for val in values["Chars"]:
        charstr=None
        l = len(val[1])
        if l > 65535:
            charstr=Nbfx.Chars32Text()
        elif l > 255:
            charstr=Nbfx.Chars16Text()
        else:
            charstr=Nbfx.Chars8Text()
        charstr.string = val[1]
        charstr.length = len(val[1])
        nbfx.records[val[0]].rec_body = charstr

    return nbfx


def nbfx_serialize(nbfx: Nbfx) -> bytes:
    return kaitai_serialize(nbfx)


def kaitai_serialize(obj: KaitaiStruct) -> bytes:
    # nbfx._check()
    # Still an ugly hack to determine expected output size
    final_size = obj._io.size()
    try:
        # This may need increasing for large messages!
        _test_io = KaitaiStream(BytesIO(bytearray(102400)))
        obj._write(_test_io)
        # print(obj._io.size(),obj._io.pos())
    except:
        final_size = _test_io.pos()
        # print("crash override", final_size)

    _out_io = KaitaiStream(BytesIO(bytearray(final_size)))
    obj._write(_out_io)
    return _out_io.to_byte_array()


def nbfx_set_string(nbfx_str: Nbfx.NbfxString, value: str):
    nbfx_str.str = value
    # nbfx_set_multibyte_int31(nbfx_str.str_len, len(value))
    nbfx_str.str_len = nbfx_get_multibyte_int31(len(value))


def nbfx_get_multibyte_int31(value: int) -> Nbfx.MultiByteInt31:
    mb = OldMultiByteInt31()
    mb.value = value
    #print(repr(mb.to_bytes()))
    mb_io = KaitaiStream(BytesIO(mb.to_bytes()))
    nbfx_int = Nbfx.MultiByteInt31(mb_io)
    nbfx_int._read()
    return nbfx_int
