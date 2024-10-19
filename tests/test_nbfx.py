from nbfx import *
from kaitaistruct import KaitaiStream
from os import listdir
from os.path import isfile, join
import pytest

# @pytest.fixture(autouse=True)
# def change_test_dir(request, monkeypatch):
#    monkeypatch.chdir(request.fspath.dirname)

sample_files = [
    join("samples", f) for f in listdir("samples") if isfile(join("samples", f))
]


@pytest.fixture()
def nbfx_from_file(file):
    with KaitaiStream(open(file, "rb")) as _io:
        nbfx = Nbfx(_io)
        nbfx._read()
        yield nbfx


def reserialize_size(nbfx, size):
    vals = nbfx_export_values(nbfx)
    new_vals = {"Dictionary": [], "NbfxString": [], "Number": []}
    for val in vals["Dictionary"]:
        new_vals["Dictionary"].append((val[0], "A" * size))
    nbfx1=nbfx_import_values(nbfx, new_vals)
    return nbfx_serialize(nbfx1)
"""
@pytest.mark.parametrize("file", sample_files)
@pytest.mark.parametrize("size,expected", [(5521, b"\x91+A"), (145, b"\x91\x01A")])
def test_reserialize_str_len_2bytes(nbfx_from_file, size, expected):
    assert expected in reserialize_size(nbfx_from_file, size)
"""

@pytest.mark.parametrize("file", sample_files)
@pytest.mark.parametrize("size,expected", [(17, b"\x11A")])
def test_reserialize_str_len_1byte(nbfx_from_file, size, expected):
    assert expected in reserialize_size(nbfx_from_file, size)
"""
@pytest.mark.parametrize("value,expected", [(145,[0x99,0x01])])
def test_multibyte(value,expected):
    mb=nbfx_get_multibyte_int31(value)
    print(repr(nbfx_serialize(mb)))
    for i, val in enumerate(expected):
        assert(val == mb.multibytes[i].value)
"""
