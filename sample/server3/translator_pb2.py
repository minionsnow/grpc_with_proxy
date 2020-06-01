# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: translator.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='translator.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x10translator.proto\"#\n\x04Text\x12\r\n\x05value\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x65st\x18\x02 \x01(\t\"\x1b\n\nreturntext\x12\r\n\x05value\x18\x01 \x01(\t2/\n\nTranslator\x12!\n\tGoogTrans\x12\x05.Text\x1a\x0b.returntext\"\x00\x62\x06proto3'
)




_TEXT = _descriptor.Descriptor(
  name='Text',
  full_name='Text',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='Text.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dest', full_name='Text.dest', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=55,
)


_RETURNTEXT = _descriptor.Descriptor(
  name='returntext',
  full_name='returntext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='returntext.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=57,
  serialized_end=84,
)

DESCRIPTOR.message_types_by_name['Text'] = _TEXT
DESCRIPTOR.message_types_by_name['returntext'] = _RETURNTEXT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Text = _reflection.GeneratedProtocolMessageType('Text', (_message.Message,), {
  'DESCRIPTOR' : _TEXT,
  '__module__' : 'translator_pb2'
  # @@protoc_insertion_point(class_scope:Text)
  })
_sym_db.RegisterMessage(Text)

returntext = _reflection.GeneratedProtocolMessageType('returntext', (_message.Message,), {
  'DESCRIPTOR' : _RETURNTEXT,
  '__module__' : 'translator_pb2'
  # @@protoc_insertion_point(class_scope:returntext)
  })
_sym_db.RegisterMessage(returntext)



_TRANSLATOR = _descriptor.ServiceDescriptor(
  name='Translator',
  full_name='Translator',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=86,
  serialized_end=133,
  methods=[
  _descriptor.MethodDescriptor(
    name='GoogTrans',
    full_name='Translator.GoogTrans',
    index=0,
    containing_service=None,
    input_type=_TEXT,
    output_type=_RETURNTEXT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TRANSLATOR)

DESCRIPTOR.services_by_name['Translator'] = _TRANSLATOR

# @@protoc_insertion_point(module_scope)