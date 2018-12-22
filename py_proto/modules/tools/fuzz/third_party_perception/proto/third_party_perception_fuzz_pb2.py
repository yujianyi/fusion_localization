# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/tools/fuzz/third_party_perception/proto/third_party_perception_fuzz.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from modules.drivers.proto import mobileye_pb2 as modules_dot_drivers_dot_proto_dot_mobileye__pb2
from modules.canbus.proto import chassis_pb2 as modules_dot_canbus_dot_proto_dot_chassis__pb2
from modules.drivers.proto import delphi_esr_pb2 as modules_dot_drivers_dot_proto_dot_delphi__esr__pb2
from modules.drivers.proto import conti_radar_pb2 as modules_dot_drivers_dot_proto_dot_conti__radar__pb2
from modules.localization.proto import localization_pb2 as modules_dot_localization_dot_proto_dot_localization__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/tools/fuzz/third_party_perception/proto/third_party_perception_fuzz.proto',
  package='apollo.tools.fuzz.third_party_perception',
  syntax='proto2',
  serialized_pb=_b('\nQmodules/tools/fuzz/third_party_perception/proto/third_party_perception_fuzz.proto\x12(apollo.tools.fuzz.third_party_perception\x1a$modules/drivers/proto/mobileye.proto\x1a\"modules/canbus/proto/chassis.proto\x1a&modules/drivers/proto/delphi_esr.proto\x1a\'modules/drivers/proto/conti_radar.proto\x1a-modules/localization/proto/localization.proto\"\xa0\x02\n\x1fThirdPartyPerceptionFuzzMessage\x12*\n\x08mobileye\x18\x01 \x02(\x0b\x32\x18.apollo.drivers.Mobileye\x12\'\n\x07\x63hassis\x18\x02 \x02(\x0b\x32\x16.apollo.canbus.Chassis\x12-\n\ndelphi_esr\x18\x03 \x02(\x0b\x32\x19.apollo.drivers.DelphiESR\x12/\n\x0b\x63onti_radar\x18\x04 \x02(\x0b\x32\x1a.apollo.drivers.ContiRadar\x12H\n\x15localization_estimate\x18\x05 \x02(\x0b\x32).apollo.localization.LocalizationEstimate')
  ,
  dependencies=[modules_dot_drivers_dot_proto_dot_mobileye__pb2.DESCRIPTOR,modules_dot_canbus_dot_proto_dot_chassis__pb2.DESCRIPTOR,modules_dot_drivers_dot_proto_dot_delphi__esr__pb2.DESCRIPTOR,modules_dot_drivers_dot_proto_dot_conti__radar__pb2.DESCRIPTOR,modules_dot_localization_dot_proto_dot_localization__pb2.DESCRIPTOR,])




_THIRDPARTYPERCEPTIONFUZZMESSAGE = _descriptor.Descriptor(
  name='ThirdPartyPerceptionFuzzMessage',
  full_name='apollo.tools.fuzz.third_party_perception.ThirdPartyPerceptionFuzzMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mobileye', full_name='apollo.tools.fuzz.third_party_perception.ThirdPartyPerceptionFuzzMessage.mobileye', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chassis', full_name='apollo.tools.fuzz.third_party_perception.ThirdPartyPerceptionFuzzMessage.chassis', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delphi_esr', full_name='apollo.tools.fuzz.third_party_perception.ThirdPartyPerceptionFuzzMessage.delphi_esr', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='conti_radar', full_name='apollo.tools.fuzz.third_party_perception.ThirdPartyPerceptionFuzzMessage.conti_radar', index=3,
      number=4, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='localization_estimate', full_name='apollo.tools.fuzz.third_party_perception.ThirdPartyPerceptionFuzzMessage.localization_estimate', index=4,
      number=5, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  serialized_start=330,
  serialized_end=618,
)

_THIRDPARTYPERCEPTIONFUZZMESSAGE.fields_by_name['mobileye'].message_type = modules_dot_drivers_dot_proto_dot_mobileye__pb2._MOBILEYE
_THIRDPARTYPERCEPTIONFUZZMESSAGE.fields_by_name['chassis'].message_type = modules_dot_canbus_dot_proto_dot_chassis__pb2._CHASSIS
_THIRDPARTYPERCEPTIONFUZZMESSAGE.fields_by_name['delphi_esr'].message_type = modules_dot_drivers_dot_proto_dot_delphi__esr__pb2._DELPHIESR
_THIRDPARTYPERCEPTIONFUZZMESSAGE.fields_by_name['conti_radar'].message_type = modules_dot_drivers_dot_proto_dot_conti__radar__pb2._CONTIRADAR
_THIRDPARTYPERCEPTIONFUZZMESSAGE.fields_by_name['localization_estimate'].message_type = modules_dot_localization_dot_proto_dot_localization__pb2._LOCALIZATIONESTIMATE
DESCRIPTOR.message_types_by_name['ThirdPartyPerceptionFuzzMessage'] = _THIRDPARTYPERCEPTIONFUZZMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ThirdPartyPerceptionFuzzMessage = _reflection.GeneratedProtocolMessageType('ThirdPartyPerceptionFuzzMessage', (_message.Message,), dict(
  DESCRIPTOR = _THIRDPARTYPERCEPTIONFUZZMESSAGE,
  __module__ = 'modules.tools.fuzz.third_party_perception.proto.third_party_perception_fuzz_pb2'
  # @@protoc_insertion_point(class_scope:apollo.tools.fuzz.third_party_perception.ThirdPartyPerceptionFuzzMessage)
  ))
_sym_db.RegisterMessage(ThirdPartyPerceptionFuzzMessage)


# @@protoc_insertion_point(module_scope)
