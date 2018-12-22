# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/common/proto/drive_event.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
from modules.localization.proto import pose_pb2 as modules_dot_localization_dot_proto_dot_pose__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/common/proto/drive_event.proto',
  package='apollo.common',
  syntax='proto2',
  serialized_pb=_b('\n&modules/common/proto/drive_event.proto\x12\rapollo.common\x1a!modules/common/proto/header.proto\x1a%modules/localization/proto/pose.proto\"\xdf\x01\n\nDriveEvent\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12\r\n\x05\x65vent\x18\x02 \x01(\t\x12+\n\x08location\x18\x03 \x01(\x0b\x32\x19.apollo.localization.Pose\x12,\n\x04type\x18\x04 \x03(\x0e\x32\x1e.apollo.common.DriveEvent.Type\"@\n\x04Type\x12\x0c\n\x08\x43RITICAL\x10\x00\x12\x0b\n\x07PROBLEM\x10\x01\x12\x0b\n\x07\x44\x45SIRED\x10\x02\x12\x10\n\x0cOUT_OF_SCOPE\x10\x03')
  ,
  dependencies=[modules_dot_common_dot_proto_dot_header__pb2.DESCRIPTOR,modules_dot_localization_dot_proto_dot_pose__pb2.DESCRIPTOR,])



_DRIVEEVENT_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='apollo.common.DriveEvent.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CRITICAL', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROBLEM', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DESIRED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OUT_OF_SCOPE', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=291,
  serialized_end=355,
)
_sym_db.RegisterEnumDescriptor(_DRIVEEVENT_TYPE)


_DRIVEEVENT = _descriptor.Descriptor(
  name='DriveEvent',
  full_name='apollo.common.DriveEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='apollo.common.DriveEvent.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='event', full_name='apollo.common.DriveEvent.event', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='location', full_name='apollo.common.DriveEvent.location', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='apollo.common.DriveEvent.type', index=3,
      number=4, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DRIVEEVENT_TYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=132,
  serialized_end=355,
)

_DRIVEEVENT.fields_by_name['header'].message_type = modules_dot_common_dot_proto_dot_header__pb2._HEADER
_DRIVEEVENT.fields_by_name['location'].message_type = modules_dot_localization_dot_proto_dot_pose__pb2._POSE
_DRIVEEVENT.fields_by_name['type'].enum_type = _DRIVEEVENT_TYPE
_DRIVEEVENT_TYPE.containing_type = _DRIVEEVENT
DESCRIPTOR.message_types_by_name['DriveEvent'] = _DRIVEEVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DriveEvent = _reflection.GeneratedProtocolMessageType('DriveEvent', (_message.Message,), dict(
  DESCRIPTOR = _DRIVEEVENT,
  __module__ = 'modules.common.proto.drive_event_pb2'
  # @@protoc_insertion_point(class_scope:apollo.common.DriveEvent)
  ))
_sym_db.RegisterMessage(DriveEvent)


# @@protoc_insertion_point(module_scope)
