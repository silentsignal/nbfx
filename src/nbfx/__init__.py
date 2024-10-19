from .nbfx import Nbfx
from kaitaistruct import KaitaiStream
from io import BytesIO

__all__ = ["nbfx_export_values", "nbfx_import_values", "nbfx_serialize", "Nbfx"]


def nbfx_export_values(nbfx: Nbfx) -> dict:
    ret = {"NbfxString": [], "Number": []}
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
                ret["Number"].append((i,rec.value))
        except AttributeError:
            pass
    return ret


def nbfx_import_values(nbfx: Nbfx, values) -> Nbfx:
    for val in values["NbfxString"]:
        rec = nbfx.records[val[0]].rec_body
        nbfx_str = getattr(rec, val[1])
        nbfx_set_string(nbfx_str, val[2])
    for val in values["Number"]:
        nbfx.records[val[0]].rec_body.value=val[1]

    return nbfx


def nbfx_serialize(nbfx: Nbfx) -> bytes:
    nbfx._check()
    # Still an ugly hack to determine expected output size
    final_size = 0
    try:
        # This may need increasing for large messages!
        _test_io = KaitaiStream(BytesIO(bytearray(102400)))
        nbfx._write(_test_io)
    except:
        final_size = _test_io.pos()

    _out_io = KaitaiStream(BytesIO(bytearray(final_size)))
    nbfx._write(_out_io)
    return _out_io.to_byte_array()


def nbfx_set_string(nbfx_str: Nbfx.NbfxString, value: str):
    nbfx_str.str = value
    nbfx_set_multibyte_int31(nbfx_str.str_len, len(value))


def nbfx_set_multibyte_int31(nbfx_int: Nbfx.MultiByteInt31, value: int):
    if value <= 0x7F:
        nbfx_int.multibytes[0].value = value
        nbfx_int.multibytes[0].has_next = 0
        return
    if value > 0x7F and value <= 0x3FFF:
        nbfx_int.multibytes = []
        mb0 = Nbfx.Multibyte()
        mb0.value = value & 0x7F
        mb0.has_next = 1
        nbfx_int.multibytes.append(mb0)
        mb1 = Nbfx.Multibyte()
        mb1.value = (value & 0xFF80) >> 7
        mb1.has_next = 0
        nbfx_int.multibytes.append(mb1)
        return
