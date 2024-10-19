Python NBFX
===========

Kaitai Struct parser for the MS-NBFX format used by WCF applications.

Official docs: https://learn.microsoft.com/en-us/openspecs/windows_protocols/mc-nbfx/0487de39-1cef-4e45-a1e3-d6292bec3d61

Installation
------------

Install with `pip install .` from the project's main directory.

Usage
-----

The package can be used just like any other Kaitai parser:

```
nbfx = Nbfx.from_file(myfile)
```

If you need **serialization support**, you need to initialize the object as described in the Serialization tutorial:

```py
    with KaitaiStream(open(file, "rb")) as _io:
        nbfx = Nbfx(_io)
        nbfx._read()
```

### Editing Objects

As basic data types may be parts of complex datastrucures, maintaining data consistency (e.g. stored length vs edited string size) while editing objects can be challenging. The package conains helper functions to import/export editable data:

```py
    editable_values = nbfx_export_values(nbfx)
    # ... do something with the editable_values dictionary ...
    nbfx_import_values(nbfx, editable_values)
```

Testing
-------

Execute `pytest` to run the tests.
