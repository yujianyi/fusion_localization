# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/data/proto/warehouse_query.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from modules.data.proto import task_pb2 as modules_dot_data_dot_proto_dot_task__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/data/proto/warehouse_query.proto',
  package='apollo.data',
  syntax='proto2',
  serialized_pb=_b('\n(modules/data/proto/warehouse_query.proto\x12\x0b\x61pollo.data\x1a\x1dmodules/data/proto/task.proto\"\xa9\x01\n\rSearchRequest\x12\x14\n\x0cvehicle_name\x18\x01 \x01(\t\x12\x10\n\x08map_name\x18\x02 \x01(\t\x12-\n\tloop_type\x18\x03 \x01(\x0e\x32\x1a.apollo.data.Task.LoopType\x12\x0e\n\x06topics\x18\x04 \x03(\t\x12\x0e\n\x06\x66ields\x18\x05 \x03(\t\x12\x11\n\x05\x63ount\x18\x06 \x01(\x05:\x02\x32\x30\x12\x0e\n\x06offset\x18\x07 \x01(\x05\"G\n\x0eSearchResponse\x12 \n\x05tasks\x18\x01 \x03(\x0b\x32\x11.apollo.data.Task\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05')
  ,
  dependencies=[modules_dot_data_dot_proto_dot_task__pb2.DESCRIPTOR,])




_SEARCHREQUEST = _descriptor.Descriptor(
  name='SearchRequest',
  full_name='apollo.data.SearchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vehicle_name', full_name='apollo.data.SearchRequest.vehicle_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='map_name', full_name='apollo.data.SearchRequest.map_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='loop_type', full_name='apollo.data.SearchRequest.loop_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='topics', full_name='apollo.data.SearchRequest.topics', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fields', full_name='apollo.data.SearchRequest.fields', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='apollo.data.SearchRequest.count', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=20,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='offset', full_name='apollo.data.SearchRequest.offset', index=6,
      number=7, type=5, cpp_type=1, label=1,
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
  serialized_start=89,
  serialized_end=258,
)


_SEARCHRESPONSE = _descriptor.Descriptor(
  name='SearchResponse',
  full_name='apollo.data.SearchResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tasks', full_name='apollo.data.SearchResponse.tasks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_count', full_name='apollo.data.SearchResponse.total_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=260,
  serialized_end=331,
)

_SEARCHREQUEST.fields_by_name['loop_type'].enum_type = modules_dot_data_dot_proto_dot_task__pb2._TASK_LOOPTYPE
_SEARCHRESPONSE.fields_by_name['tasks'].message_type = modules_dot_data_dot_proto_dot_task__pb2._TASK
DESCRIPTOR.message_types_by_name['SearchRequest'] = _SEARCHREQUEST
DESCRIPTOR.message_types_by_name['SearchResponse'] = _SEARCHRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SearchRequest = _reflection.GeneratedProtocolMessageType('SearchRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHREQUEST,
  __module__ = 'modules.data.proto.warehouse_query_pb2'
  # @@protoc_insertion_point(class_scope:apollo.data.SearchRequest)
  ))
_sym_db.RegisterMessage(SearchRequest)

SearchResponse = _reflection.GeneratedProtocolMessageType('SearchResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHRESPONSE,
  __module__ = 'modules.data.proto.warehouse_query_pb2'
  # @@protoc_insertion_point(class_scope:apollo.data.SearchResponse)
  ))
_sym_db.RegisterMessage(SearchResponse)


# @@protoc_insertion_point(module_scope)
