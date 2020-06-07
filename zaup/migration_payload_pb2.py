# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: migration_payload.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='migration_payload.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x17migration_payload.proto\"\x8c\x05\n\x10MigrationPayload\x12\x37\n\x0eotp_parameters\x18\x01 \x03(\x0b\x32\x1f.MigrationPayload.OtpParameters\x12\x0f\n\x07version\x18\x02 \x01(\x05\x12\x12\n\nbatch_size\x18\x03 \x01(\x05\x12\x13\n\x0b\x62\x61tch_index\x18\x04 \x01(\x05\x12\x10\n\x08\x62\x61tch_id\x18\x05 \x01(\x05\x1a\xd5\x01\n\rOtpParameters\x12\x0e\n\x06secret\x18\x01 \x01(\x0c\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06issuer\x18\x03 \x01(\t\x12.\n\talgorithm\x18\x04 \x01(\x0e\x32\x1b.MigrationPayload.Algorithm\x12,\n\x06\x64igits\x18\x05 \x01(\x0e\x32\x1c.MigrationPayload.DigitCount\x12\'\n\x04type\x18\x06 \x01(\x0e\x32\x19.MigrationPayload.OtpType\x12\x0f\n\x07\x63ounter\x18\x07 \x01(\x03\"y\n\tAlgorithm\x12\x19\n\x15\x41LGORITHM_UNSPECIFIED\x10\x00\x12\x12\n\x0e\x41LGORITHM_SHA1\x10\x01\x12\x14\n\x10\x41LGORITHM_SHA256\x10\x02\x12\x14\n\x10\x41LGORITHM_SHA512\x10\x03\x12\x11\n\rALGORITHM_MD5\x10\x04\"U\n\nDigitCount\x12\x1b\n\x17\x44IGIT_COUNT_UNSPECIFIED\x10\x00\x12\x13\n\x0f\x44IGIT_COUNT_SIX\x10\x01\x12\x15\n\x11\x44IGIT_COUNT_EIGHT\x10\x02\"I\n\x07OtpType\x12\x18\n\x14OTP_TYPE_UNSPECIFIED\x10\x00\x12\x11\n\rOTP_TYPE_HOTP\x10\x01\x12\x11\n\rOTP_TYPE_TOTP\x10\x02\x62\x06proto3'
)



_MIGRATIONPAYLOAD_ALGORITHM = _descriptor.EnumDescriptor(
  name='Algorithm',
  full_name='MigrationPayload.Algorithm',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ALGORITHM_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALGORITHM_SHA1', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALGORITHM_SHA256', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALGORITHM_SHA512', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALGORITHM_MD5', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=397,
  serialized_end=518,
)
_sym_db.RegisterEnumDescriptor(_MIGRATIONPAYLOAD_ALGORITHM)

_MIGRATIONPAYLOAD_DIGITCOUNT = _descriptor.EnumDescriptor(
  name='DigitCount',
  full_name='MigrationPayload.DigitCount',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DIGIT_COUNT_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DIGIT_COUNT_SIX', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DIGIT_COUNT_EIGHT', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=520,
  serialized_end=605,
)
_sym_db.RegisterEnumDescriptor(_MIGRATIONPAYLOAD_DIGITCOUNT)

_MIGRATIONPAYLOAD_OTPTYPE = _descriptor.EnumDescriptor(
  name='OtpType',
  full_name='MigrationPayload.OtpType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OTP_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OTP_TYPE_HOTP', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OTP_TYPE_TOTP', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=607,
  serialized_end=680,
)
_sym_db.RegisterEnumDescriptor(_MIGRATIONPAYLOAD_OTPTYPE)


_MIGRATIONPAYLOAD_OTPPARAMETERS = _descriptor.Descriptor(
  name='OtpParameters',
  full_name='MigrationPayload.OtpParameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='secret', full_name='MigrationPayload.OtpParameters.secret', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='MigrationPayload.OtpParameters.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='issuer', full_name='MigrationPayload.OtpParameters.issuer', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='algorithm', full_name='MigrationPayload.OtpParameters.algorithm', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='digits', full_name='MigrationPayload.OtpParameters.digits', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='MigrationPayload.OtpParameters.type', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='counter', full_name='MigrationPayload.OtpParameters.counter', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=182,
  serialized_end=395,
)

_MIGRATIONPAYLOAD = _descriptor.Descriptor(
  name='MigrationPayload',
  full_name='MigrationPayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='otp_parameters', full_name='MigrationPayload.otp_parameters', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='MigrationPayload.version', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='batch_size', full_name='MigrationPayload.batch_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='batch_index', full_name='MigrationPayload.batch_index', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='batch_id', full_name='MigrationPayload.batch_id', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_MIGRATIONPAYLOAD_OTPPARAMETERS, ],
  enum_types=[
    _MIGRATIONPAYLOAD_ALGORITHM,
    _MIGRATIONPAYLOAD_DIGITCOUNT,
    _MIGRATIONPAYLOAD_OTPTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=680,
)

_MIGRATIONPAYLOAD_OTPPARAMETERS.fields_by_name['algorithm'].enum_type = _MIGRATIONPAYLOAD_ALGORITHM
_MIGRATIONPAYLOAD_OTPPARAMETERS.fields_by_name['digits'].enum_type = _MIGRATIONPAYLOAD_DIGITCOUNT
_MIGRATIONPAYLOAD_OTPPARAMETERS.fields_by_name['type'].enum_type = _MIGRATIONPAYLOAD_OTPTYPE
_MIGRATIONPAYLOAD_OTPPARAMETERS.containing_type = _MIGRATIONPAYLOAD
_MIGRATIONPAYLOAD.fields_by_name['otp_parameters'].message_type = _MIGRATIONPAYLOAD_OTPPARAMETERS
_MIGRATIONPAYLOAD_ALGORITHM.containing_type = _MIGRATIONPAYLOAD
_MIGRATIONPAYLOAD_DIGITCOUNT.containing_type = _MIGRATIONPAYLOAD
_MIGRATIONPAYLOAD_OTPTYPE.containing_type = _MIGRATIONPAYLOAD
DESCRIPTOR.message_types_by_name['MigrationPayload'] = _MIGRATIONPAYLOAD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MigrationPayload = _reflection.GeneratedProtocolMessageType('MigrationPayload', (_message.Message,), {

  'OtpParameters' : _reflection.GeneratedProtocolMessageType('OtpParameters', (_message.Message,), {
    'DESCRIPTOR' : _MIGRATIONPAYLOAD_OTPPARAMETERS,
    '__module__' : 'migration_payload_pb2'
    # @@protoc_insertion_point(class_scope:MigrationPayload.OtpParameters)
    })
  ,
  'DESCRIPTOR' : _MIGRATIONPAYLOAD,
  '__module__' : 'migration_payload_pb2'
  # @@protoc_insertion_point(class_scope:MigrationPayload)
  })
_sym_db.RegisterMessage(MigrationPayload)
_sym_db.RegisterMessage(MigrationPayload.OtpParameters)


# @@protoc_insertion_point(module_scope)
