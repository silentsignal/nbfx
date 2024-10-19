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


class MultiByteInt31(object):
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
    ret = {"Dictionary": [], "NbfxString": [], "Number": []}
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
    orig_dict_len = len(kaitai_serialize(nbfx.dictionary_table.entries))
    dict_mb = MultiByteInt31()
    dict_mb.value = orig_dict_len
    orig_table_len=orig_dict_len+len(dict_mb.to_bytes())

    orig_nbfx_len = len(kaitai_serialize(nbfx))
    
    #print("Original dict length", orig_dict_len)
    for val in values["Dictionary"]:
        nbfx_str = nbfx.dictionary_table.entries.entry[val[0]]
        nbfx_set_string(nbfx_str, val[1])
        nbfx.dictionary_table.entries.entry[val[0]] = nbfx_str
    dict_len = len(kaitai_serialize(nbfx.dictionary_table.entries))
    #print("dict_len", dict_len)
    #nbfx_set_multibyte_int31(nbfx.dictionary_table.size, dict_len)
    nbfx.dictionary_table.size = nbfx_get_multibyte_int31(dict_len)
    #print("new dict length set to", nbfx.dictionary_table.size.value)

    mb = MultiByteInt31()
    mb.value = dict_len
    correct_size = dict_len + len(mb.to_bytes())
    #print("correct_size", correct_size)
    #print(dict_len, correct_size)

    #print(correct_size, nbfx.dictionary_table.entries._io.size(), nbfx.dictionary_table._io.size())
    new_io = KaitaiStream(BytesIO(bytearray(correct_size)))
    #nbfx.dictionary_table._io = new_io
    # nbfx.dictionary_table._write(new_io)
    #new_io.seek(0)
    #print(correct_size, nbfx.dictionary_table.entries._io.size(), nbfx.dictionary_table._io.size())
    #new_entries_io = KaitaiStream(BytesIO(bytearray(dict_len)))
    #nbfx.dictionary_table.entries._io = new_entries_io
    # nbfx.dictionary_table.entries._write(new_entries_io)
    #new_entries_io.seek(0)
    #print(correct_size, nbfx.dictionary_table.entries._io.size(), nbfx.dictionary_table._io.size())

    """
    new_nbfx_len=orig_nbfx_len-(orig_table_len-correct_size)
    new_nbfx_io=KaitaiStream(BytesIO(bytearray(new_nbfx_len)))
    nbfx._io=new_nbfx_io
    new_nbfx_io.seek(0)
    print("nbfx",orig_nbfx_len,new_nbfx_len)
    """

    """
    for val in values["NbfxString"]:
        rec = nbfx.records[val[0]].rec_body
        nbfx_str = getattr(rec, val[1])
        nbfx_set_string(nbfx_str, val[2])
    for val in values["Number"]:
        nbfx.records[val[0]].rec_body.value = val[1]
    """
    return nbfx


def nbfx_serialize(nbfx: Nbfx) -> bytes:
    """
    entries_bytes=kaitai_serialize(nbfx.dictionary_table.entries)
    print(repr(entries_bytes))
    entries_size=len(entries_bytes)
    mb=MultiByteInt31()
    mb.value=entries_size
    dict_size_bytes=mb.to_bytes()
    print(repr(dict_size_bytes))
    records_bytes=b''
    for rec in nbfx.records:
        records_bytes+=kaitai_serialize(rec)
    return dict_size_bytes+entries_bytes+records_bytes
    """
    return kaitai_serialize(nbfx)


def kaitai_serialize(obj: KaitaiStruct) -> bytes:
    # nbfx._check()
    # Still an ugly hack to determine expected output size
    print("ser",obj._io.size())
    final_size = 0
    try:
        # This may need increasing for large messages!
        _test_io = KaitaiStream(BytesIO(bytearray(102400)))
        obj._write(_test_io)
    except:
        final_size = _test_io.pos()

    _out_io = KaitaiStream(BytesIO(bytearray(final_size)))
    obj._write(_out_io)
    return _out_io.to_byte_array()


def nbfx_set_string(nbfx_str: Nbfx.NbfxString, value: str):
    nbfx_str.str = value
    #nbfx_set_multibyte_int31(nbfx_str.str_len, len(value))
    nbfx_str.str_len = nbfx_get_multibyte_int31(len(value))

"""
def nbfx_set_multibyte_int31(nbfx_int: Nbfx.MultiByteInt31, value: int):
    print("old", nbfx_int.value, "to", value)
    # nbfx_int.multibytes.clear()
    mb = MultiByteInt31()
    mb.value = value
    mb_io = KaitaiStream(BytesIO(mb.to_bytes()))
    nbfx_int = Nbfx.MultiByteInt31(mb_io)
    nbfx_int._read()
"""

"""
    while value > 0:
        mb_io=KaitaiStream(BytesIO(bytearray(2)))
        mb=Nbfx.Multibyte(mb_io)
        mb._io=mb_io
        mb._read()
        mb._parent=nbfx_int
        mb.value = value & 0x7f
        #print(hex(mb.value))
        value = value >> 7
        if value > 0:
            mb.has_next = 1
        else:
            mb.has_next = 0 
        nbfx_int.multibytes.append(mb)
    nbfx_int._invalidate_last()
    nbfx_int._invalidate_value()
"""


"""
    if value <= 0x7F:
        nbfx_int.multibytes[0].value = value
        nbfx_int.multibytes[0].has_next = 0
        nbfx_int._invalidate_last()
        nbfx_int._invalidate_value()

        new_io=KaitaiStream(BytesIO(bytearray(2)))
        #nbfx_int._io=new_io
        nbfx_int._write(new_io)
        new_io.seek(0)

        print("new(1b)",nbfx_int.value)
        return
    if value > 0x7F and value <= 0x3FFF:
        nbfx_int.multibytes = []
        mb0=init_io(Nbfx.Multibyte, 2)
        mb0.value = value & 0x7F
        mb0.dummy="mb0"
        mb0.has_next = 1
        nbfx_int.multibytes.append(mb0)
        mb1=init_io(Nbfx.Multibyte,2)
        mb1.dummy="mb1"
        mb1._read()
        mb1.value = (value & 0x7f) << 7
        mb1.has_next = 0
        nbfx_int.multibytes.append(mb1)

        nbfx_int._invalidate_last()
        #nbfx_int._invalidate_value()

        new_io=KaitaiStream(BytesIO(bytearray(2)))
        nbfx_int._io=new_io
        nbfx_int._write(new_io)
        new_io.seek(0)

        print("new",nbfx_int.value)
        return
"""


def nbfx_get_multibyte_int31(value: int) -> Nbfx.MultiByteInt31:
    mb = MultiByteInt31()
    mb.value = value
    mb_io = KaitaiStream(BytesIO(mb.to_bytes()))
    nbfx_int = Nbfx.MultiByteInt31(mb_io)
    nbfx_int._read()
    return nbfx_int


    """
    ret = Nbfx.MultiByteInt31(KaitaiStream(BytesIO(b"\x00")))
    ret._read()
    ret.multibytes.clear()
    while value > 0:
        mb = init_io(Nbfx.Multibyte, 2)
        mb._parent = ret
        mb.value = value & 0x7F
        print(hex(mb.value))
        value = value >> 7
        if value > 0:
            mb.has_next = 1
        else:
            mb.has_next = 0
        ret.multibytes.append(mb)
    return ret
    """

def init_io(cls, size):
    obj = cls()
    new_io = KaitaiStream(BytesIO(bytearray(size)))
    obj._io = new_io
    obj._write(new_io)
    new_io.seek(0)
    return obj
