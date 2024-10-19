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

@pytest.mark.parametrize("file", sample_files)
def test_reserialize_str_len_2bytes(nbfx_from_file):
    vals = nbfx_export_values(nbfx_from_file)
    new_vals = []
    for val in vals:
        new_vals.append((val[0], val[1], "A" * 5521))
    nbfx_import_values(nbfx_from_file, new_vals)
    result = nbfx_serialize(nbfx_from_file)
    assert b"\x91+AAAA" in result
