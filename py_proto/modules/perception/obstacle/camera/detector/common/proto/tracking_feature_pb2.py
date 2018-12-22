# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/perception/obstacle/camera/detector/common/proto/tracking_feature.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/perception/obstacle/camera/detector/common/proto/tracking_feature.proto',
  package='apollo.perception',
  syntax='proto2',
  serialized_pb=_b('\nOmodules/perception/obstacle/camera/detector/common/proto/tracking_feature.proto\x12\x11\x61pollo.perception\"r\n\x0c\x46\x65\x61tureParam\x12\x17\n\x0b\x66\x65\x61t_stride\x18\x01 \x01(\x05:\x02\x33\x32\x12\x34\n\textractor\x18\x02 \x03(\x0b\x32!.apollo.perception.ExtractorParam\x12\x13\n\x0bremap_model\x18\x03 \x01(\t\"\x89\x02\n\x0e\x45xtractorParam\x12\x11\n\tfeat_blob\x18\x01 \x01(\t\x12G\n\tfeat_type\x18\x02 \x01(\x0e\x32-.apollo.perception.ExtractorParam.FeatureType:\x05Reorg\x12=\n\x11roi_pooling_param\x18\x03 \x01(\x0b\x32\".apollo.perception.ROIPoolingParam\x12\x32\n\x0breorg_param\x18\x04 \x01(\x0b\x32\x1d.apollo.perception.ReorgParam\"(\n\x0b\x46\x65\x61tureType\x12\t\n\x05Reorg\x10\x00\x12\x0e\n\nROIPooling\x10\x01\"U\n\x0fROIPoolingParam\x12\x13\n\x08pooled_h\x18\x01 \x01(\x05:\x01\x33\x12\x13\n\x08pooled_w\x18\x02 \x01(\x05:\x01\x33\x12\x18\n\tuse_floor\x18\x03 \x01(\x08:\x05\x66\x61lse\"9\n\nReorgParam\x12\x15\n\nref_height\x18\x01 \x01(\x05:\x01\x30\x12\x14\n\tref_width\x18\x02 \x01(\x05:\x01\x30')
)



_EXTRACTORPARAM_FEATURETYPE = _descriptor.EnumDescriptor(
  name='FeatureType',
  full_name='apollo.perception.ExtractorParam.FeatureType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Reorg', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROIPooling', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=444,
  serialized_end=484,
)
_sym_db.RegisterEnumDescriptor(_EXTRACTORPARAM_FEATURETYPE)


_FEATUREPARAM = _descriptor.Descriptor(
  name='FeatureParam',
  full_name='apollo.perception.FeatureParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feat_stride', full_name='apollo.perception.FeatureParam.feat_stride', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=32,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='extractor', full_name='apollo.perception.FeatureParam.extractor', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='remap_model', full_name='apollo.perception.FeatureParam.remap_model', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=102,
  serialized_end=216,
)


_EXTRACTORPARAM = _descriptor.Descriptor(
  name='ExtractorParam',
  full_name='apollo.perception.ExtractorParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feat_blob', full_name='apollo.perception.ExtractorParam.feat_blob', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='feat_type', full_name='apollo.perception.ExtractorParam.feat_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='roi_pooling_param', full_name='apollo.perception.ExtractorParam.roi_pooling_param', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reorg_param', full_name='apollo.perception.ExtractorParam.reorg_param', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _EXTRACTORPARAM_FEATURETYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=219,
  serialized_end=484,
)


_ROIPOOLINGPARAM = _descriptor.Descriptor(
  name='ROIPoolingParam',
  full_name='apollo.perception.ROIPoolingParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pooled_h', full_name='apollo.perception.ROIPoolingParam.pooled_h', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=3,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pooled_w', full_name='apollo.perception.ROIPoolingParam.pooled_w', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=3,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_floor', full_name='apollo.perception.ROIPoolingParam.use_floor', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
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
  serialized_start=486,
  serialized_end=571,
)


_REORGPARAM = _descriptor.Descriptor(
  name='ReorgParam',
  full_name='apollo.perception.ReorgParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ref_height', full_name='apollo.perception.ReorgParam.ref_height', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ref_width', full_name='apollo.perception.ReorgParam.ref_width', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
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
  serialized_start=573,
  serialized_end=630,
)

_FEATUREPARAM.fields_by_name['extractor'].message_type = _EXTRACTORPARAM
_EXTRACTORPARAM.fields_by_name['feat_type'].enum_type = _EXTRACTORPARAM_FEATURETYPE
_EXTRACTORPARAM.fields_by_name['roi_pooling_param'].message_type = _ROIPOOLINGPARAM
_EXTRACTORPARAM.fields_by_name['reorg_param'].message_type = _REORGPARAM
_EXTRACTORPARAM_FEATURETYPE.containing_type = _EXTRACTORPARAM
DESCRIPTOR.message_types_by_name['FeatureParam'] = _FEATUREPARAM
DESCRIPTOR.message_types_by_name['ExtractorParam'] = _EXTRACTORPARAM
DESCRIPTOR.message_types_by_name['ROIPoolingParam'] = _ROIPOOLINGPARAM
DESCRIPTOR.message_types_by_name['ReorgParam'] = _REORGPARAM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FeatureParam = _reflection.GeneratedProtocolMessageType('FeatureParam', (_message.Message,), dict(
  DESCRIPTOR = _FEATUREPARAM,
  __module__ = 'modules.perception.obstacle.camera.detector.common.proto.tracking_feature_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.FeatureParam)
  ))
_sym_db.RegisterMessage(FeatureParam)

ExtractorParam = _reflection.GeneratedProtocolMessageType('ExtractorParam', (_message.Message,), dict(
  DESCRIPTOR = _EXTRACTORPARAM,
  __module__ = 'modules.perception.obstacle.camera.detector.common.proto.tracking_feature_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.ExtractorParam)
  ))
_sym_db.RegisterMessage(ExtractorParam)

ROIPoolingParam = _reflection.GeneratedProtocolMessageType('ROIPoolingParam', (_message.Message,), dict(
  DESCRIPTOR = _ROIPOOLINGPARAM,
  __module__ = 'modules.perception.obstacle.camera.detector.common.proto.tracking_feature_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.ROIPoolingParam)
  ))
_sym_db.RegisterMessage(ROIPoolingParam)

ReorgParam = _reflection.GeneratedProtocolMessageType('ReorgParam', (_message.Message,), dict(
  DESCRIPTOR = _REORGPARAM,
  __module__ = 'modules.perception.obstacle.camera.detector.common.proto.tracking_feature_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.ReorgParam)
  ))
_sym_db.RegisterMessage(ReorgParam)


# @@protoc_insertion_point(module_scope)
