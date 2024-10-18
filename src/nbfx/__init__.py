from .nbfx import Nbfx
from kaitaistruct import KaitaiStream
from io import BytesIO

__all__ = ["nbfx_export_values", "nbfx_import_values", "nbfx_serialize", "Nbfx"]


def nbfx_export_values(nbfx: Nbfx) -> list:
    ret = []
    for i, record in enumerate(nbfx.records):
        try:
            rec = record.rec_body
            if isinstance(rec, Nbfx.PrefixAttribute):
                ret.append((i, "name", rec.name.str))
                ret.append((i, "value", rec.value.str))
            elif isinstance(rec, Nbfx.DictionaryAttribute):
                ret.append((i, "prefix", rec.prefix.str))
        except AttributeError:
            pass
    return ret


def nbfx_import_values(nbfx: Nbfx, values) -> Nbfx:
    for val in values:
        rec = nbfx.records[val[0]].rec_body
        nbfx_str = getattr(rec, val[1])
        nbfx_set_string(nbfx_str, val[2])
    return nbfx


def nbfx_serialize(nbfx: Nbfx) -> bytes:
    nbfx._check()
    final_size = 0
    try:
        _test_io = KaitaiStream(BytesIO(bytearray(1024)))
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
    if value <= 0x7f:
        nbfx_int.multibytes[0].value = value
        nbfx_int.multibytes[0].has_next = 0
        return
