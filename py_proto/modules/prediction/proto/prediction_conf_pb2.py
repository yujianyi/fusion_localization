# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/prediction/proto/prediction_conf.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from modules.perception.proto import perception_obstacle_pb2 as modules_dot_perception_dot_proto_dot_perception__obstacle__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/prediction/proto/prediction_conf.proto',
  package='apollo.prediction',
  syntax='proto2',
  serialized_pb=_b('\n.modules/prediction/proto/prediction_conf.proto\x12\x11\x61pollo.prediction\x1a\x32modules/perception/proto/perception_obstacle.proto\"\xe9\x04\n\x0cObstacleConf\x12\x41\n\robstacle_type\x18\x01 \x01(\x0e\x32*.apollo.perception.PerceptionObstacle.Type\x12G\n\x0fobstacle_status\x18\x02 \x01(\x0e\x32..apollo.prediction.ObstacleConf.ObstacleStatus\x12\x45\n\x0e\x65valuator_type\x18\x03 \x01(\x0e\x32-.apollo.prediction.ObstacleConf.EvaluatorType\x12\x45\n\x0epredictor_type\x18\x04 \x01(\x0e\x32-.apollo.prediction.ObstacleConf.PredictorType\"G\n\x0eObstacleStatus\x12\x0b\n\x07ON_LANE\x10\x00\x12\x0c\n\x08OFF_LANE\x10\x01\x12\x0e\n\nSTATIONARY\x10\x03\x12\n\n\x06MOVING\x10\x04\"I\n\rEvaluatorType\x12\x11\n\rMLP_EVALUATOR\x10\x00\x12\x11\n\rRNN_EVALUATOR\x10\x01\x12\x12\n\x0e\x43OST_EVALUATOR\x10\x02\"\xaa\x01\n\rPredictorType\x12\x1b\n\x17LANE_SEQUENCE_PREDICTOR\x10\x00\x12\x17\n\x13\x46REE_MOVE_PREDICTOR\x10\x01\x12\x16\n\x12REGIONAL_PREDICTOR\x10\x02\x12\x1b\n\x17MOVE_SEQUENCE_PREDICTOR\x10\x03\x12\x13\n\x0f\x45MPTY_PREDICTOR\x10\x04\x12\x19\n\x15SINGLE_LANE_PREDICTOR\x10\x05\"H\n\x0ePredictionConf\x12\x36\n\robstacle_conf\x18\x01 \x03(\x0b\x32\x1f.apollo.prediction.ObstacleConf')
  ,
  dependencies=[modules_dot_perception_dot_proto_dot_perception__obstacle__pb2.DESCRIPTOR,])



_OBSTACLECONF_OBSTACLESTATUS = _descriptor.EnumDescriptor(
  name='ObstacleStatus',
  full_name='apollo.prediction.ObstacleConf.ObstacleStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ON_LANE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OFF_LANE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATIONARY', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOVING', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=420,
  serialized_end=491,
)
_sym_db.RegisterEnumDescriptor(_OBSTACLECONF_OBSTACLESTATUS)

_OBSTACLECONF_EVALUATORTYPE = _descriptor.EnumDescriptor(
  name='EvaluatorType',
  full_name='apollo.prediction.ObstacleConf.EvaluatorType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MLP_EVALUATOR', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RNN_EVALUATOR', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COST_EVALUATOR', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=493,
  serialized_end=566,
)
_sym_db.RegisterEnumDescriptor(_OBSTACLECONF_EVALUATORTYPE)

_OBSTACLECONF_PREDICTORTYPE = _descriptor.EnumDescriptor(
  name='PredictorType',
  full_name='apollo.prediction.ObstacleConf.PredictorType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LANE_SEQUENCE_PREDICTOR', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FREE_MOVE_PREDICTOR', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REGIONAL_PREDICTOR', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOVE_SEQUENCE_PREDICTOR', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMPTY_PREDICTOR', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SINGLE_LANE_PREDICTOR', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=569,
  serialized_end=739,
)
_sym_db.RegisterEnumDescriptor(_OBSTACLECONF_PREDICTORTYPE)


_OBSTACLECONF = _descriptor.Descriptor(
  name='ObstacleConf',
  full_name='apollo.prediction.ObstacleConf',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='obstacle_type', full_name='apollo.prediction.ObstacleConf.obstacle_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='obstacle_status', full_name='apollo.prediction.ObstacleConf.obstacle_status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='evaluator_type', full_name='apollo.prediction.ObstacleConf.evaluator_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='predictor_type', full_name='apollo.prediction.ObstacleConf.predictor_type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _OBSTACLECONF_OBSTACLESTATUS,
    _OBSTACLECONF_EVALUATORTYPE,
    _OBSTACLECONF_PREDICTORTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=122,
  serialized_end=739,
)


_PREDICTIONCONF = _descriptor.Descriptor(
  name='PredictionConf',
  full_name='apollo.prediction.PredictionConf',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='obstacle_conf', full_name='apollo.prediction.PredictionConf.obstacle_conf', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=741,
  serialized_end=813,
)

_OBSTACLECONF.fields_by_name['obstacle_type'].enum_type = modules_dot_perception_dot_proto_dot_perception__obstacle__pb2._PERCEPTIONOBSTACLE_TYPE
_OBSTACLECONF.fields_by_name['obstacle_status'].enum_type = _OBSTACLECONF_OBSTACLESTATUS
_OBSTACLECONF.fields_by_name['evaluator_type'].enum_type = _OBSTACLECONF_EVALUATORTYPE
_OBSTACLECONF.fields_by_name['predictor_type'].enum_type = _OBSTACLECONF_PREDICTORTYPE
_OBSTACLECONF_OBSTACLESTATUS.containing_type = _OBSTACLECONF
_OBSTACLECONF_EVALUATORTYPE.containing_type = _OBSTACLECONF
_OBSTACLECONF_PREDICTORTYPE.containing_type = _OBSTACLECONF
_PREDICTIONCONF.fields_by_name['obstacle_conf'].message_type = _OBSTACLECONF
DESCRIPTOR.message_types_by_name['ObstacleConf'] = _OBSTACLECONF
DESCRIPTOR.message_types_by_name['PredictionConf'] = _PREDICTIONCONF
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ObstacleConf = _reflection.GeneratedProtocolMessageType('ObstacleConf', (_message.Message,), dict(
  DESCRIPTOR = _OBSTACLECONF,
  __module__ = 'modules.prediction.proto.prediction_conf_pb2'
  # @@protoc_insertion_point(class_scope:apollo.prediction.ObstacleConf)
  ))
_sym_db.RegisterMessage(ObstacleConf)

PredictionConf = _reflection.GeneratedProtocolMessageType('PredictionConf', (_message.Message,), dict(
  DESCRIPTOR = _PREDICTIONCONF,
  __module__ = 'modules.prediction.proto.prediction_conf_pb2'
  # @@protoc_insertion_point(class_scope:apollo.prediction.PredictionConf)
  ))
_sym_db.RegisterMessage(PredictionConf)


# @@protoc_insertion_point(module_scope)
