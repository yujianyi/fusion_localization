# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/perception/proto/perception_map_roi.proto

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
from modules.map.proto import map_pb2 as modules_dot_map_dot_proto_dot_map__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/perception/proto/perception_map_roi.proto',
  package='apollo.perception',
  syntax='proto2',
  serialized_pb=_b('\n1modules/perception/proto/perception_map_roi.proto\x12\x11\x61pollo.perception\x1a!modules/common/proto/header.proto\x1a\x1bmodules/map/proto/map.proto\"\xe5\x02\n\x10PerceptionMapROI\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12*\n\x0chdmap_header\x18\x08 \x01(\x0b\x32\x14.apollo.hdmap.Header\x12\x10\n\x08origin_x\x18\x02 \x01(\x01\x12\x10\n\x08origin_y\x18\x03 \x01(\x01\x12\x11\n\tgrid_size\x18\x04 \x01(\x01\x12\x10\n\x08num_rows\x18\x05 \x01(\x05\x12\x13\n\x0bnum_columns\x18\x06 \x01(\x05\x12:\n\x06region\x18\x07 \x03(\x0b\x32*.apollo.perception.PerceptionMapROI.Region\x1a\x64\n\x06Region\x12\x0f\n\x07start_x\x18\x01 \x01(\x05\x12\r\n\x05\x65nd_x\x18\x02 \x01(\x05\x12\x0f\n\x07start_y\x18\x03 \x01(\x05\x12\r\n\x05\x65nd_y\x18\x04 \x01(\x05\x12\x1a\n\x12\x65xtension_distance\x18\x05 \x01(\x05')
  ,
  dependencies=[modules_dot_common_dot_proto_dot_header__pb2.DESCRIPTOR,modules_dot_map_dot_proto_dot_map__pb2.DESCRIPTOR,])




_PERCEPTIONMAPROI_REGION = _descriptor.Descriptor(
  name='Region',
  full_name='apollo.perception.PerceptionMapROI.Region',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_x', full_name='apollo.perception.PerceptionMapROI.Region.start_x', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_x', full_name='apollo.perception.PerceptionMapROI.Region.end_x', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_y', full_name='apollo.perception.PerceptionMapROI.Region.start_y', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_y', full_name='apollo.perception.PerceptionMapROI.Region.end_y', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='extension_distance', full_name='apollo.perception.PerceptionMapROI.Region.extension_distance', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=394,
  serialized_end=494,
)

_PERCEPTIONMAPROI = _descriptor.Descriptor(
  name='PerceptionMapROI',
  full_name='apollo.perception.PerceptionMapROI',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='apollo.perception.PerceptionMapROI.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hdmap_header', full_name='apollo.perception.PerceptionMapROI.hdmap_header', index=1,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='origin_x', full_name='apollo.perception.PerceptionMapROI.origin_x', index=2,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='origin_y', full_name='apollo.perception.PerceptionMapROI.origin_y', index=3,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='grid_size', full_name='apollo.perception.PerceptionMapROI.grid_size', index=4,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_rows', full_name='apollo.perception.PerceptionMapROI.num_rows', index=5,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_columns', full_name='apollo.perception.PerceptionMapROI.num_columns', index=6,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='region', full_name='apollo.perception.PerceptionMapROI.region', index=7,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PERCEPTIONMAPROI_REGION, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=137,
  serialized_end=494,
)

_PERCEPTIONMAPROI_REGION.containing_type = _PERCEPTIONMAPROI
_PERCEPTIONMAPROI.fields_by_name['header'].message_type = modules_dot_common_dot_proto_dot_header__pb2._HEADER
_PERCEPTIONMAPROI.fields_by_name['hdmap_header'].message_type = modules_dot_map_dot_proto_dot_map__pb2._HEADER
_PERCEPTIONMAPROI.fields_by_name['region'].message_type = _PERCEPTIONMAPROI_REGION
DESCRIPTOR.message_types_by_name['PerceptionMapROI'] = _PERCEPTIONMAPROI
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PerceptionMapROI = _reflection.GeneratedProtocolMessageType('PerceptionMapROI', (_message.Message,), dict(

  Region = _reflection.GeneratedProtocolMessageType('Region', (_message.Message,), dict(
    DESCRIPTOR = _PERCEPTIONMAPROI_REGION,
    __module__ = 'modules.perception.proto.perception_map_roi_pb2'
    # @@protoc_insertion_point(class_scope:apollo.perception.PerceptionMapROI.Region)
    ))
  ,
  DESCRIPTOR = _PERCEPTIONMAPROI,
  __module__ = 'modules.perception.proto.perception_map_roi_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.PerceptionMapROI)
  ))
_sym_db.RegisterMessage(PerceptionMapROI)
_sym_db.RegisterMessage(PerceptionMapROI.Region)


# @@protoc_insertion_point(module_scope)
