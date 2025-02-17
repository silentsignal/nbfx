Python NBFX
===========
![build and test workflow](https://github.com/silentsignal/nbfx/actions/workflows/python-app.yml/badge.svg)

Kaitai Struct parser for the MC-NBFX format used by WCF applications.

Official docs: https://learn.microsoft.com/en-us/openspecs/windows_protocols/mc-nbfx/0487de39-1cef-4e45-a1e3-d6292bec3d61

Related blog post with some more details about the design and implementation: https://blog.silentsignal.eu/2024/10/28/wcf-net.tcp-pentest/

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

### Dictionary Tables

The parser and the associated helper functions are _stateless_: we don't keep track of dictionary entries, only include their index numbers in the (de)serialized objects. This reduces complexity and improves reliability (see dictionary handling bugs of python-wcfbin). If you want to manipulate strings in the dictionary cache you either have to edit its first occurrance, or rebuild the NBFX stream so it'll contain string records instead of dictionary references. If you want to generate a nice textual XML representation of the messages, you'll need to build your dictionary cache around this package (again, python-wcfbin has an example, but it's buggy).

Testing
-------

Execute `pytest` to run the tests.
