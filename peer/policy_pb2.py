# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: peer/policy.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common import policies_pb2 as common_dot_policies__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='peer/policy.proto',
  package='protos',
  syntax='proto3',
  serialized_pb=_b('\n\x11peer/policy.proto\x12\x06protos\x1a\x15\x63ommon/policies.proto\"\x83\x01\n\x11\x41pplicationPolicy\x12;\n\x10signature_policy\x18\x01 \x01(\x0b\x32\x1f.common.SignaturePolicyEnvelopeH\x00\x12)\n\x1f\x63hannel_config_policy_reference\x18\x02 \x01(\tH\x00\x42\x06\n\x04TypeBR\n\"org.hyperledger.fabric.protos.peerZ,github.com/hyperledger/fabric-protos-go/peerb\x06proto3')
  ,
  dependencies=[common_dot_policies__pb2.DESCRIPTOR,])




_APPLICATIONPOLICY = _descriptor.Descriptor(
  name='ApplicationPolicy',
  full_name='protos.ApplicationPolicy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='signature_policy', full_name='protos.ApplicationPolicy.signature_policy', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel_config_policy_reference', full_name='protos.ApplicationPolicy.channel_config_policy_reference', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='Type', full_name='protos.ApplicationPolicy.Type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=53,
  serialized_end=184,
)

_APPLICATIONPOLICY.fields_by_name['signature_policy'].message_type = common_dot_policies__pb2._SIGNATUREPOLICYENVELOPE
_APPLICATIONPOLICY.oneofs_by_name['Type'].fields.append(
  _APPLICATIONPOLICY.fields_by_name['signature_policy'])
_APPLICATIONPOLICY.fields_by_name['signature_policy'].containing_oneof = _APPLICATIONPOLICY.oneofs_by_name['Type']
_APPLICATIONPOLICY.oneofs_by_name['Type'].fields.append(
  _APPLICATIONPOLICY.fields_by_name['channel_config_policy_reference'])
_APPLICATIONPOLICY.fields_by_name['channel_config_policy_reference'].containing_oneof = _APPLICATIONPOLICY.oneofs_by_name['Type']
DESCRIPTOR.message_types_by_name['ApplicationPolicy'] = _APPLICATIONPOLICY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ApplicationPolicy = _reflection.GeneratedProtocolMessageType('ApplicationPolicy', (_message.Message,), dict(
  DESCRIPTOR = _APPLICATIONPOLICY,
  __module__ = 'peer.policy_pb2'
  # @@protoc_insertion_point(class_scope:protos.ApplicationPolicy)
  ))
_sym_db.RegisterMessage(ApplicationPolicy)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\"org.hyperledger.fabric.protos.peerZ,github.com/hyperledger/fabric-protos-go/peer'))
# @@protoc_insertion_point(module_scope)
