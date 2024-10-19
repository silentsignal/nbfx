# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Nbfx(ReadWriteKaitaiStruct):
    def __init__(self, _io=None, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self

    def _read(self):
        self.dictionary_table = Nbfx.DictionaryTable(self._io, self, self._root)
        self.dictionary_table._read()
        self.records = []
        i = 0
        while not self._io.is_eof():
            _t_records = Nbfx.Record(self._io, self, self._root)
            _t_records._read()
            self.records.append(_t_records)
            i += 1



    def _fetch_instances(self):
        pass
        self.dictionary_table._fetch_instances()
        for i in range(len(self.records)):
            pass
            self.records[i]._fetch_instances()



    def _write__seq(self, io=None):
        super(Nbfx, self)._write__seq(io)
        self.dictionary_table._write__seq(self._io)
        for i in range(len(self.records)):
            pass
            if self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"records", self._io.size() - self._io.pos(), 0)
            self.records[i]._write__seq(self._io)

        if not self._io.is_eof():
            raise kaitaistruct.ConsistencyError(u"records", self._io.size() - self._io.pos(), 0)


    def _check(self):
        pass
        if self.dictionary_table._root != self._root:
            raise kaitaistruct.ConsistencyError(u"dictionary_table", self.dictionary_table._root, self._root)
        if self.dictionary_table._parent != self:
            raise kaitaistruct.ConsistencyError(u"dictionary_table", self.dictionary_table._parent, self)
        for i in range(len(self.records)):
            pass
            if self.records[i]._root != self._root:
                raise kaitaistruct.ConsistencyError(u"records", self.records[i]._root, self._root)
            if self.records[i]._parent != self:
                raise kaitaistruct.ConsistencyError(u"records", self.records[i]._parent, self)


    class PrefixDictionaryElement(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.name_id = Nbfx.MultiByteInt31(self._io, self, self._root)
            self.name_id._read()


        def _fetch_instances(self):
            pass
            self.name_id._fetch_instances()


        def _write__seq(self, io=None):
            super(Nbfx.PrefixDictionaryElement, self)._write__seq(io)
            self.name_id._write__seq(self._io)


        def _check(self):
            pass
            if self.name_id._root != self._root:
                raise kaitaistruct.ConsistencyError(u"name_id", self.name_id._root, self._root)
            if self.name_id._parent != self:
                raise kaitaistruct.ConsistencyError(u"name_id", self.name_id._parent, self)


    class ShortDictionaryXmlnsAttribute(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.value = Nbfx.MultiByteInt31(self._io, self, self._root)
            self.value._read()


        def _fetch_instances(self):
            pass
            self.value._fetch_instances()


        def _write__seq(self, io=None):
            super(Nbfx.ShortDictionaryXmlnsAttribute, self)._write__seq(io)
            self.value._write__seq(self._io)


        def _check(self):
            pass
            if self.value._root != self._root:
                raise kaitaistruct.ConsistencyError(u"value", self.value._root, self._root)
            if self.value._parent != self:
                raise kaitaistruct.ConsistencyError(u"value", self.value._parent, self)


    class MultiByteInt31(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.multibytes = []
            i = 0
            while True:
                _t_multibytes = Nbfx.Multibyte(self._io, self, self._root)
                _t_multibytes._read()
                _ = _t_multibytes
                self.multibytes.append(_)
                if not (_.has_next):
                    break
                i += 1


        def _fetch_instances(self):
            pass
            for i in range(len(self.multibytes)):
                pass
                self.multibytes[i]._fetch_instances()



        def _write__seq(self, io=None):
            super(Nbfx.MultiByteInt31, self)._write__seq(io)
            for i in range(len(self.multibytes)):
                pass
                self.multibytes[i]._write__seq(self._io)



        def _check(self):
            pass
            if (len(self.multibytes) == 0):
                raise kaitaistruct.ConsistencyError(u"multibytes", len(self.multibytes), 0)
            for i in range(len(self.multibytes)):
                pass
                if self.multibytes[i]._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"multibytes", self.multibytes[i]._root, self._root)
                if self.multibytes[i]._parent != self:
                    raise kaitaistruct.ConsistencyError(u"multibytes", self.multibytes[i]._parent, self)
                _ = self.multibytes[i]
                if (not (_.has_next) != (i == (len(self.multibytes) - 1))):
                    raise kaitaistruct.ConsistencyError(u"multibytes", not (_.has_next), (i == (len(self.multibytes) - 1)))


        @property
        def last(self):
            if hasattr(self, '_m_last'):
                return self._m_last

            self._m_last = (len(self.multibytes) - 1)
            return getattr(self, '_m_last', None)

        def _invalidate_last(self):
            del self._m_last
        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = (((self.multibytes[0].value | ((self.multibytes[1].value << 7) if (self.last >= 1) else 0)) | ((self.multibytes[2].value << 14) if (self.last >= 2) else 0)) | ((self.multibytes[3].value << 21) if (self.last >= 3) else 0))
            return getattr(self, '_m_value', None)

        def _invalidate_value(self):
            del self._m_value

    class XmlnsAttribute(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.prefix = Nbfx.NbfxString(self._io, self, self._root)
            self.prefix._read()
            self.name = Nbfx.NbfxString(self._io, self, self._root)
            self.name._read()


        def _fetch_instances(self):
            pass
            self.prefix._fetch_instances()
            self.name._fetch_instances()


        def _write__seq(self, io=None):
            super(Nbfx.XmlnsAttribute, self)._write__seq(io)
            self.prefix._write__seq(self._io)
            self.name._write__seq(self._io)


        def _check(self):
            pass
            if self.prefix._root != self._root:
                raise kaitaistruct.ConsistencyError(u"prefix", self.prefix._root, self._root)
            if self.prefix._parent != self:
                raise kaitaistruct.ConsistencyError(u"prefix", self.prefix._parent, self)
            if self.name._root != self._root:
                raise kaitaistruct.ConsistencyError(u"name", self.name._root, self._root)
            if self.name._parent != self:
                raise kaitaistruct.ConsistencyError(u"name", self.name._parent, self)


    class DictionaryEntries(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.entry = []
            i = 0
            while not self._io.is_eof():
                _t_entry = Nbfx.NbfxString(self._io, self, self._root)
                _t_entry._read()
                self.entry.append(_t_entry)
                i += 1



        def _fetch_instances(self):
            pass
            for i in range(len(self.entry)):
                pass
                self.entry[i]._fetch_instances()



        def _write__seq(self, io=None):
            super(Nbfx.DictionaryEntries, self)._write__seq(io)
            for i in range(len(self.entry)):
                pass
                if self._io.is_eof():
                    raise kaitaistruct.ConsistencyError(u"entry", self._io.size() - self._io.pos(), 0)
                self.entry[i]._write__seq(self._io)

            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"entry", self._io.size() - self._io.pos(), 0)


        def _check(self):
            pass
            for i in range(len(self.entry)):
                pass
                if self.entry[i]._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"entry", self.entry[i]._root, self._root)
                if self.entry[i]._parent != self:
                    raise kaitaistruct.ConsistencyError(u"entry", self.entry[i]._parent, self)



    class Multibyte(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.has_next = self._io.read_bits_int_be(1) != 0
            self.value = self._io.read_bits_int_be(7)


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Nbfx.Multibyte, self)._write__seq(io)
            self._io.write_bits_int_be(1, int(self.has_next))
            self._io.write_bits_int_be(7, self.value)


        def _check(self):
            pass


    class Int32Text(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.value = self._io.read_u4le()


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Nbfx.Int32Text, self)._write__seq(io)
            self._io.write_u4le(self.value)


        def _check(self):
            pass


    class UnknownByte(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.value = self._io.read_u1()


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Nbfx.UnknownByte, self)._write__seq(io)
            self._io.write_u1(self.value)


        def _check(self):
            pass


    class ShortDictionaryElement(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.name_id = Nbfx.MultiByteInt31(self._io, self, self._root)
            self.name_id._read()


        def _fetch_instances(self):
            pass
            self.name_id._fetch_instances()


        def _write__seq(self, io=None):
            super(Nbfx.ShortDictionaryElement, self)._write__seq(io)
            self.name_id._write__seq(self._io)


        def _check(self):
            pass
            if self.name_id._root != self._root:
                raise kaitaistruct.ConsistencyError(u"name_id", self.name_id._root, self._root)
            if self.name_id._parent != self:
                raise kaitaistruct.ConsistencyError(u"name_id", self.name_id._parent, self)


    class DictionaryXmlsAttribute(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.prefix = self._io.read_u2le()
            self.value = Nbfx.MultiByteInt31(self._io, self, self._root)
            self.value._read()


        def _fetch_instances(self):
            pass
            self.value._fetch_instances()


        def _write__seq(self, io=None):
            super(Nbfx.DictionaryXmlsAttribute, self)._write__seq(io)
            self._io.write_u2le(self.prefix)
            self.value._write__seq(self._io)


        def _check(self):
            pass
            if self.value._root != self._root:
                raise kaitaistruct.ConsistencyError(u"value", self.value._root, self._root)
            if self.value._parent != self:
                raise kaitaistruct.ConsistencyError(u"value", self.value._parent, self)


    class DictionaryText(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.string_id = Nbfx.MultiByteInt31(self._io, self, self._root)
            self.string_id._read()


        def _fetch_instances(self):
            pass
            self.string_id._fetch_instances()


        def _write__seq(self, io=None):
            super(Nbfx.DictionaryText, self)._write__seq(io)
            self.string_id._write__seq(self._io)


        def _check(self):
            pass
            if self.string_id._root != self._root:
                raise kaitaistruct.ConsistencyError(u"string_id", self.string_id._root, self._root)
            if self.string_id._parent != self:
                raise kaitaistruct.ConsistencyError(u"string_id", self.string_id._parent, self)


    class OneText(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root

        def _read(self):
            pass


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Nbfx.OneText, self)._write__seq(io)


        def _check(self):
            pass


    class DictionaryTable(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.size = Nbfx.MultiByteInt31(self._io, self, self._root)
            self.size._read()
            self._raw_entries = self._io.read_bytes(self.size.value)
            _io__raw_entries = KaitaiStream(BytesIO(self._raw_entries))
            self.entries = Nbfx.DictionaryEntries(_io__raw_entries, self, self._root)
            self.entries._read()


        def _fetch_instances(self):
            pass
            self.size._fetch_instances()
            self.entries._fetch_instances()


        def _write__seq(self, io=None):
            super(Nbfx.DictionaryTable, self)._write__seq(io)
            self.size._write__seq(self._io)
            _io__raw_entries = KaitaiStream(BytesIO(bytearray(self.size.value)))
            self._io.add_child_stream(_io__raw_entries)
            _pos2 = self._io.pos()
            self._io.seek(self._io.pos() + (self.size.value))
            def handler(parent, _io__raw_entries=_io__raw_entries):
                self._raw_entries = _io__raw_entries.to_byte_array()
                if (len(self._raw_entries) != self.size.value):
                    raise kaitaistruct.ConsistencyError(u"raw(entries)", len(self._raw_entries), self.size.value)
                parent.write_bytes(self._raw_entries)
            _io__raw_entries.write_back_handler = KaitaiStream.WriteBackHandler(_pos2, handler)
            self.entries._write__seq(_io__raw_entries)


        def _check(self):
            pass
            if self.size._root != self._root:
                raise kaitaistruct.ConsistencyError(u"size", self.size._root, self._root)
            if self.size._parent != self:
                raise kaitaistruct.ConsistencyError(u"size", self.size._parent, self)
            if self.entries._root != self._root:
                raise kaitaistruct.ConsistencyError(u"entries", self.entries._root, self._root)
            if self.entries._parent != self:
                raise kaitaistruct.ConsistencyError(u"entries", self.entries._parent, self)


    class PrefixAttribute(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.name = Nbfx.NbfxString(self._io, self, self._root)
            self.name._read()
            self.value = Nbfx.NbfxString(self._io, self, self._root)
            self.value._read()


        def _fetch_instances(self):
            pass
            self.name._fetch_instances()
            self.value._fetch_instances()


        def _write__seq(self, io=None):
            super(Nbfx.PrefixAttribute, self)._write__seq(io)
            self.name._write__seq(self._io)
            self.value._write__seq(self._io)


        def _check(self):
            pass
            if self.name._root != self._root:
                raise kaitaistruct.ConsistencyError(u"name", self.name._root, self._root)
            if self.name._parent != self:
                raise kaitaistruct.ConsistencyError(u"name", self.name._parent, self)
            if self.value._root != self._root:
                raise kaitaistruct.ConsistencyError(u"value", self.value._root, self._root)
            if self.value._parent != self:
                raise kaitaistruct.ConsistencyError(u"value", self.value._parent, self)


    class Chars8Text(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.length = self._io.read_u1()
            self.bytes = self._io.read_bytes(self.length)


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Nbfx.Chars8Text, self)._write__seq(io)
            self._io.write_u1(self.length)
            self._io.write_bytes(self.bytes)


        def _check(self):
            pass
            if (len(self.bytes) != self.length):
                raise kaitaistruct.ConsistencyError(u"bytes", len(self.bytes), self.length)


    class NbfxString(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.str_len = Nbfx.MultiByteInt31(self._io, self, self._root)
            self.str_len._read()
            self.str = (self._io.read_bytes(self.str_len.value)).decode("ASCII")


        def _fetch_instances(self):
            pass
            self.str_len._fetch_instances()


        def _write__seq(self, io=None):
            super(Nbfx.NbfxString, self)._write__seq(io)
            self.str_len._write__seq(self._io)
            self._io.write_bytes((self.str).encode(u"ASCII"))


        def _check(self):
            pass
            if self.str_len._root != self._root:
                raise kaitaistruct.ConsistencyError(u"str_len", self.str_len._root, self._root)
            if self.str_len._parent != self:
                raise kaitaistruct.ConsistencyError(u"str_len", self.str_len._parent, self)
            if (len((self.str).encode(u"ASCII")) != self.str_len.value):
                raise kaitaistruct.ConsistencyError(u"str", len((self.str).encode(u"ASCII")), self.str_len.value)


    class FloatText(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.value = self._io.read_u4le()


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Nbfx.FloatText, self)._write__seq(io)
            self._io.write_u4le(self.value)


        def _check(self):
            pass


    class Int8Text(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.value = self._io.read_u1()


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Nbfx.Int8Text, self)._write__seq(io)
            self._io.write_u1(self.value)


        def _check(self):
            pass


    class Int16Text(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.value = self._io.read_u2le()


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Nbfx.Int16Text, self)._write__seq(io)
            self._io.write_u2le(self.value)


        def _check(self):
            pass


    class UniqueidText(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.uuid = self._io.read_bytes(16)


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Nbfx.UniqueidText, self)._write__seq(io)
            self._io.write_bytes(self.uuid)


        def _check(self):
            pass
            if (len(self.uuid) != 16):
                raise kaitaistruct.ConsistencyError(u"uuid", len(self.uuid), 16)


    class PrefixDictionaryAttribute(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.name_id = Nbfx.MultiByteInt31(self._io, self, self._root)
            self.name_id._read()


        def _fetch_instances(self):
            pass
            self.name_id._fetch_instances()


        def _write__seq(self, io=None):
            super(Nbfx.PrefixDictionaryAttribute, self)._write__seq(io)
            self.name_id._write__seq(self._io)


        def _check(self):
            pass
            if self.name_id._root != self._root:
                raise kaitaistruct.ConsistencyError(u"name_id", self.name_id._root, self._root)
            if self.name_id._parent != self:
                raise kaitaistruct.ConsistencyError(u"name_id", self.name_id._parent, self)


    class Record(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.rec_type = self._io.read_u1()
            _on = self.rec_type
            if _on == 141:
                pass
                self.rec_body = Nbfx.Int32Text(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 14:
                pass
                self.rec_body = Nbfx.PrefixDictionaryAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 61:
                pass
                self.rec_body = Nbfx.PrefixAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 10:
                pass
                self.rec_body = Nbfx.ShortDictionaryXmlnsAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 17:
                pass
                self.rec_body = Nbfx.PrefixDictionaryAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 146:
                pass
                self.rec_body = Nbfx.DoubleText(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 47:
                pass
                self.rec_body = Nbfx.PrefixAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 136:
                pass
                self.rec_body = Nbfx.Int8Text(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 73:
                pass
                self.rec_body = Nbfx.PrefixDictionaryElement(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 42:
                pass
                self.rec_body = Nbfx.PrefixAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 46:
                pass
                self.rec_body = Nbfx.PrefixAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 81:
                pass
                self.rec_body = Nbfx.PrefixDictionaryElement(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 39:
                pass
                self.rec_body = Nbfx.PrefixAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 60:
                pass
                self.rec_body = Nbfx.PrefixAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 24:
                pass
                self.rec_body = Nbfx.PrefixDictionaryAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 35:
                pass
                self.rec_body = Nbfx.PrefixDictionaryAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 62:
                pass
                self.rec_body = Nbfx.PrefixAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 20:
                pass
                self.rec_body = Nbfx.PrefixDictionaryAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 32:
                pass
                self.rec_body = Nbfx.PrefixDictionaryAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 7:
                pass
                self.rec_body = Nbfx.DictionaryAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 1:
                pass
                self.rec_body = Nbfx.EndElement(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 55:
                pass
                self.rec_body = Nbfx.PrefixAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 27:
                pass
                self.rec_body = Nbfx.PrefixDictionaryAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 77:
                pass
                self.rec_body = Nbfx.PrefixDictionaryElement(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 13:
                pass
                self.rec_body = Nbfx.PrefixDictionaryAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 145:
                pass
                self.rec_body = Nbfx.FloatText(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 52:
                pass
                self.rec_body = Nbfx.PrefixAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 56:
                pass
                self.rec_body = Nbfx.PrefixAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 144:
                pass
                self.rec_body = Nbfx.FloatText(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 45:
                pass
                self.rec_body = Nbfx.PrefixAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 66:
                pass
                self.rec_body = Nbfx.ShortDictionaryElement(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 85:
                pass
                self.rec_body = Nbfx.PrefixDictionaryElement(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 11:
                pass
                self.rec_body = Nbfx.DictionaryXmlsAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 69:
                pass
                self.rec_body = Nbfx.PrefixDictionaryElement(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 137:
                pass
                self.rec_body = Nbfx.Int8Text(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 12:
                pass
                self.rec_body = Nbfx.PrefixDictionaryAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 59:
                pass
                self.rec_body = Nbfx.PrefixAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 138:
                pass
                self.rec_body = Nbfx.Int16Text(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 58:
                pass
                self.rec_body = Nbfx.PrefixAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 33:
                pass
                self.rec_body = Nbfx.PrefixDictionaryAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 82:
                pass
                self.rec_body = Nbfx.PrefixDictionaryElement(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 86:
                pass
                self.rec_body = Nbfx.PrefixDictionaryElement(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 19:
                pass
                self.rec_body = Nbfx.PrefixDictionaryAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 84:
                pass
                self.rec_body = Nbfx.PrefixDictionaryElement(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 63:
                pass
                self.rec_body = Nbfx.PrefixAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 51:
                pass
                self.rec_body = Nbfx.PrefixAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 23:
                pass
                self.rec_body = Nbfx.PrefixDictionaryAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 83:
                pass
                self.rec_body = Nbfx.PrefixDictionaryElement(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 48:
                pass
                self.rec_body = Nbfx.PrefixAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 153:
                pass
                self.rec_body = Nbfx.Chars8Text(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 78:
                pass
                self.rec_body = Nbfx.PrefixDictionaryElement(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 53:
                pass
                self.rec_body = Nbfx.PrefixAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 15:
                pass
                self.rec_body = Nbfx.PrefixDictionaryAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 38:
                pass
                self.rec_body = Nbfx.PrefixAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 40:
                pass
                self.rec_body = Nbfx.PrefixAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 152:
                pass
                self.rec_body = Nbfx.Chars8Text(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 44:
                pass
                self.rec_body = Nbfx.PrefixAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 76:
                pass
                self.rec_body = Nbfx.PrefixDictionaryElement(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 79:
                pass
                self.rec_body = Nbfx.PrefixDictionaryElement(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 57:
                pass
                self.rec_body = Nbfx.PrefixAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 140:
                pass
                self.rec_body = Nbfx.Int32Text(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 9:
                pass
                self.rec_body = Nbfx.XmlnsAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 172:
                pass
                self.rec_body = Nbfx.UniqueidText(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 130:
                pass
                self.rec_body = Nbfx.OneText(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 21:
                pass
                self.rec_body = Nbfx.PrefixDictionaryAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 170:
                pass
                self.rec_body = Nbfx.DictionaryText(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 37:
                pass
                self.rec_body = Nbfx.PrefixDictionaryAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 41:
                pass
                self.rec_body = Nbfx.PrefixAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 72:
                pass
                self.rec_body = Nbfx.PrefixDictionaryElement(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 71:
                pass
                self.rec_body = Nbfx.PrefixDictionaryElement(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 171:
                pass
                self.rec_body = Nbfx.DictionaryText(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 36:
                pass
                self.rec_body = Nbfx.PrefixDictionaryAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 70:
                pass
                self.rec_body = Nbfx.PrefixDictionaryElement(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 28:
                pass
                self.rec_body = Nbfx.PrefixDictionaryAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 74:
                pass
                self.rec_body = Nbfx.PrefixDictionaryElement(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 16:
                pass
                self.rec_body = Nbfx.PrefixDictionaryAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 147:
                pass
                self.rec_body = Nbfx.DoubleText(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 18:
                pass
                self.rec_body = Nbfx.PrefixDictionaryAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 80:
                pass
                self.rec_body = Nbfx.PrefixDictionaryElement(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 68:
                pass
                self.rec_body = Nbfx.PrefixDictionaryElement(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 26:
                pass
                self.rec_body = Nbfx.PrefixDictionaryAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 139:
                pass
                self.rec_body = Nbfx.Int16Text(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 31:
                pass
                self.rec_body = Nbfx.PrefixDictionaryAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 49:
                pass
                self.rec_body = Nbfx.PrefixAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 34:
                pass
                self.rec_body = Nbfx.PrefixDictionaryAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 54:
                pass
                self.rec_body = Nbfx.PrefixAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 29:
                pass
                self.rec_body = Nbfx.PrefixDictionaryAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 75:
                pass
                self.rec_body = Nbfx.PrefixDictionaryElement(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 25:
                pass
                self.rec_body = Nbfx.PrefixDictionaryAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 43:
                pass
                self.rec_body = Nbfx.PrefixAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 50:
                pass
                self.rec_body = Nbfx.PrefixAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 22:
                pass
                self.rec_body = Nbfx.PrefixDictionaryAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 30:
                pass
                self.rec_body = Nbfx.PrefixDictionaryAttribute(self._io, self, self._root)
                self.rec_body._read()
            elif _on == 173:
                pass
                self.rec_body = Nbfx.UniqueidText(self._io, self, self._root)
                self.rec_body._read()


        def _fetch_instances(self):
            pass
            _on = self.rec_type
            if _on == 141:
                pass
                self.rec_body._fetch_instances()
            elif _on == 14:
                pass
                self.rec_body._fetch_instances()
            elif _on == 61:
                pass
                self.rec_body._fetch_instances()
            elif _on == 10:
                pass
                self.rec_body._fetch_instances()
            elif _on == 17:
                pass
                self.rec_body._fetch_instances()
            elif _on == 146:
                pass
                self.rec_body._fetch_instances()
            elif _on == 47:
                pass
                self.rec_body._fetch_instances()
            elif _on == 136:
                pass
                self.rec_body._fetch_instances()
            elif _on == 73:
                pass
                self.rec_body._fetch_instances()
            elif _on == 42:
                pass
                self.rec_body._fetch_instances()
            elif _on == 46:
                pass
                self.rec_body._fetch_instances()
            elif _on == 81:
                pass
                self.rec_body._fetch_instances()
            elif _on == 39:
                pass
                self.rec_body._fetch_instances()
            elif _on == 60:
                pass
                self.rec_body._fetch_instances()
            elif _on == 24:
                pass
                self.rec_body._fetch_instances()
            elif _on == 35:
                pass
                self.rec_body._fetch_instances()
            elif _on == 62:
                pass
                self.rec_body._fetch_instances()
            elif _on == 20:
                pass
                self.rec_body._fetch_instances()
            elif _on == 32:
                pass
                self.rec_body._fetch_instances()
            elif _on == 7:
                pass
                self.rec_body._fetch_instances()
            elif _on == 1:
                pass
                self.rec_body._fetch_instances()
            elif _on == 55:
                pass
                self.rec_body._fetch_instances()
            elif _on == 27:
                pass
                self.rec_body._fetch_instances()
            elif _on == 77:
                pass
                self.rec_body._fetch_instances()
            elif _on == 13:
                pass
                self.rec_body._fetch_instances()
            elif _on == 145:
                pass
                self.rec_body._fetch_instances()
            elif _on == 52:
                pass
                self.rec_body._fetch_instances()
            elif _on == 56:
                pass
                self.rec_body._fetch_instances()
            elif _on == 144:
                pass
                self.rec_body._fetch_instances()
            elif _on == 45:
                pass
                self.rec_body._fetch_instances()
            elif _on == 66:
                pass
                self.rec_body._fetch_instances()
            elif _on == 85:
                pass
                self.rec_body._fetch_instances()
            elif _on == 11:
                pass
                self.rec_body._fetch_instances()
            elif _on == 69:
                pass
                self.rec_body._fetch_instances()
            elif _on == 137:
                pass
                self.rec_body._fetch_instances()
            elif _on == 12:
                pass
                self.rec_body._fetch_instances()
            elif _on == 59:
                pass
                self.rec_body._fetch_instances()
            elif _on == 138:
                pass
                self.rec_body._fetch_instances()
            elif _on == 58:
                pass
                self.rec_body._fetch_instances()
            elif _on == 33:
                pass
                self.rec_body._fetch_instances()
            elif _on == 82:
                pass
                self.rec_body._fetch_instances()
            elif _on == 86:
                pass
                self.rec_body._fetch_instances()
            elif _on == 19:
                pass
                self.rec_body._fetch_instances()
            elif _on == 84:
                pass
                self.rec_body._fetch_instances()
            elif _on == 63:
                pass
                self.rec_body._fetch_instances()
            elif _on == 51:
                pass
                self.rec_body._fetch_instances()
            elif _on == 23:
                pass
                self.rec_body._fetch_instances()
            elif _on == 83:
                pass
                self.rec_body._fetch_instances()
            elif _on == 48:
                pass
                self.rec_body._fetch_instances()
            elif _on == 153:
                pass
                self.rec_body._fetch_instances()
            elif _on == 78:
                pass
                self.rec_body._fetch_instances()
            elif _on == 53:
                pass
                self.rec_body._fetch_instances()
            elif _on == 15:
                pass
                self.rec_body._fetch_instances()
            elif _on == 38:
                pass
                self.rec_body._fetch_instances()
            elif _on == 40:
                pass
                self.rec_body._fetch_instances()
            elif _on == 152:
                pass
                self.rec_body._fetch_instances()
            elif _on == 44:
                pass
                self.rec_body._fetch_instances()
            elif _on == 76:
                pass
                self.rec_body._fetch_instances()
            elif _on == 79:
                pass
                self.rec_body._fetch_instances()
            elif _on == 57:
                pass
                self.rec_body._fetch_instances()
            elif _on == 140:
                pass
                self.rec_body._fetch_instances()
            elif _on == 9:
                pass
                self.rec_body._fetch_instances()
            elif _on == 172:
                pass
                self.rec_body._fetch_instances()
            elif _on == 130:
                pass
                self.rec_body._fetch_instances()
            elif _on == 21:
                pass
                self.rec_body._fetch_instances()
            elif _on == 170:
                pass
                self.rec_body._fetch_instances()
            elif _on == 37:
                pass
                self.rec_body._fetch_instances()
            elif _on == 41:
                pass
                self.rec_body._fetch_instances()
            elif _on == 72:
                pass
                self.rec_body._fetch_instances()
            elif _on == 71:
                pass
                self.rec_body._fetch_instances()
            elif _on == 171:
                pass
                self.rec_body._fetch_instances()
            elif _on == 36:
                pass
                self.rec_body._fetch_instances()
            elif _on == 70:
                pass
                self.rec_body._fetch_instances()
            elif _on == 28:
                pass
                self.rec_body._fetch_instances()
            elif _on == 74:
                pass
                self.rec_body._fetch_instances()
            elif _on == 16:
                pass
                self.rec_body._fetch_instances()
            elif _on == 147:
                pass
                self.rec_body._fetch_instances()
            elif _on == 18:
                pass
                self.rec_body._fetch_instances()
            elif _on == 80:
                pass
                self.rec_body._fetch_instances()
            elif _on == 68:
                pass
                self.rec_body._fetch_instances()
            elif _on == 26:
                pass
                self.rec_body._fetch_instances()
            elif _on == 139:
                pass
                self.rec_body._fetch_instances()
            elif _on == 31:
                pass
                self.rec_body._fetch_instances()
            elif _on == 49:
                pass
                self.rec_body._fetch_instances()
            elif _on == 34:
                pass
                self.rec_body._fetch_instances()
            elif _on == 54:
                pass
                self.rec_body._fetch_instances()
            elif _on == 29:
                pass
                self.rec_body._fetch_instances()
            elif _on == 75:
                pass
                self.rec_body._fetch_instances()
            elif _on == 25:
                pass
                self.rec_body._fetch_instances()
            elif _on == 43:
                pass
                self.rec_body._fetch_instances()
            elif _on == 50:
                pass
                self.rec_body._fetch_instances()
            elif _on == 22:
                pass
                self.rec_body._fetch_instances()
            elif _on == 30:
                pass
                self.rec_body._fetch_instances()
            elif _on == 173:
                pass
                self.rec_body._fetch_instances()


        def _write__seq(self, io=None):
            super(Nbfx.Record, self)._write__seq(io)
            self._io.write_u1(self.rec_type)
            _on = self.rec_type
            if _on == 141:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 14:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 61:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 10:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 17:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 146:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 47:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 136:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 73:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 42:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 46:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 81:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 39:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 60:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 24:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 35:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 62:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 20:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 32:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 7:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 1:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 55:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 27:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 77:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 13:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 145:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 52:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 56:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 144:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 45:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 66:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 85:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 11:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 69:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 137:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 12:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 59:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 138:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 58:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 33:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 82:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 86:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 19:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 84:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 63:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 51:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 23:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 83:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 48:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 153:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 78:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 53:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 15:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 38:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 40:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 152:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 44:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 76:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 79:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 57:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 140:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 9:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 172:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 130:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 21:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 170:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 37:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 41:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 72:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 71:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 171:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 36:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 70:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 28:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 74:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 16:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 147:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 18:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 80:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 68:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 26:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 139:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 31:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 49:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 34:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 54:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 29:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 75:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 25:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 43:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 50:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 22:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 30:
                pass
                self.rec_body._write__seq(self._io)
            elif _on == 173:
                pass
                self.rec_body._write__seq(self._io)


        def _check(self):
            pass
            _on = self.rec_type
            if _on == 141:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 14:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 61:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 10:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 17:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 146:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 47:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 136:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 73:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 42:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 46:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 81:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 39:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 60:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 24:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 35:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 62:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 20:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 32:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 7:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 1:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 55:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 27:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 77:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 13:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 145:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 52:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 56:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 144:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 45:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 66:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 85:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 11:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 69:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 137:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 12:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 59:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 138:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 58:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 33:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 82:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 86:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 19:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 84:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 63:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 51:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 23:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 83:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 48:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 153:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 78:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 53:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 15:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 38:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 40:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 152:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 44:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 76:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 79:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 57:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 140:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 9:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 172:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 130:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 21:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 170:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 37:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 41:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 72:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 71:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 171:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 36:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 70:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 28:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 74:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 16:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 147:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 18:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 80:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 68:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 26:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 139:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 31:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 49:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 34:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 54:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 29:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 75:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 25:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 43:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 50:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 22:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 30:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)
            elif _on == 173:
                pass
                if self.rec_body._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._root, self._root)
                if self.rec_body._parent != self:
                    raise kaitaistruct.ConsistencyError(u"rec_body", self.rec_body._parent, self)


    class DictionaryAttribute(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.prefix = Nbfx.NbfxString(self._io, self, self._root)
            self.prefix._read()
            self.name = Nbfx.MultiByteInt31(self._io, self, self._root)
            self.name._read()
            self.value = Nbfx.Record(self._io, self, self._root)
            self.value._read()


        def _fetch_instances(self):
            pass
            self.prefix._fetch_instances()
            self.name._fetch_instances()
            self.value._fetch_instances()


        def _write__seq(self, io=None):
            super(Nbfx.DictionaryAttribute, self)._write__seq(io)
            self.prefix._write__seq(self._io)
            self.name._write__seq(self._io)
            self.value._write__seq(self._io)


        def _check(self):
            pass
            if self.prefix._root != self._root:
                raise kaitaistruct.ConsistencyError(u"prefix", self.prefix._root, self._root)
            if self.prefix._parent != self:
                raise kaitaistruct.ConsistencyError(u"prefix", self.prefix._parent, self)
            if self.name._root != self._root:
                raise kaitaistruct.ConsistencyError(u"name", self.name._root, self._root)
            if self.name._parent != self:
                raise kaitaistruct.ConsistencyError(u"name", self.name._parent, self)
            if self.value._root != self._root:
                raise kaitaistruct.ConsistencyError(u"value", self.value._root, self._root)
            if self.value._parent != self:
                raise kaitaistruct.ConsistencyError(u"value", self.value._parent, self)


    class EndElement(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root

        def _read(self):
            pass


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Nbfx.EndElement, self)._write__seq(io)


        def _check(self):
            pass


    class DoubleText(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.value = self._io.read_u8le()


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Nbfx.DoubleText, self)._write__seq(io)
            self._io.write_u8le(self.value)


        def _check(self):
            pass



