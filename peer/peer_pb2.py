# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: peer/peer.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from peer import proposal_pb2 as peer_dot_proposal__pb2
from peer import proposal_response_pb2 as peer_dot_proposal__response__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='peer/peer.proto',
  package='protos',
  syntax='proto3',
  serialized_pb=_b('\n\x0fpeer/peer.proto\x12\x06protos\x1a\x13peer/proposal.proto\x1a\x1cpeer/proposal_response.proto2O\n\x08\x45ndorser\x12\x43\n\x0fProcessProposal\x12\x16.protos.SignedProposal\x1a\x18.protos.ProposalResponseBR\n\"org.hyperledger.fabric.protos.peerZ,github.com/hyperledger/fabric-protos-go/peerb\x06proto3')
  ,
  dependencies=[peer_dot_proposal__pb2.DESCRIPTOR,peer_dot_proposal__response__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\"org.hyperledger.fabric.protos.peerZ,github.com/hyperledger/fabric-protos-go/peer'))

_ENDORSER = _descriptor.ServiceDescriptor(
  name='Endorser',
  full_name='protos.Endorser',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=78,
  serialized_end=157,
  methods=[
  _descriptor.MethodDescriptor(
    name='ProcessProposal',
    full_name='protos.Endorser.ProcessProposal',
    index=0,
    containing_service=None,
    input_type=peer_dot_proposal__pb2._SIGNEDPROPOSAL,
    output_type=peer_dot_proposal__response__pb2._PROPOSALRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ENDORSER)

DESCRIPTOR.services_by_name['Endorser'] = _ENDORSER

# @@protoc_insertion_point(module_scope)
