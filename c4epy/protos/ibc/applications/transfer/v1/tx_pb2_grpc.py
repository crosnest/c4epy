# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ibc.applications.transfer.v1 import (
    tx_pb2 as ibc_dot_applications_dot_transfer_dot_v1_dot_tx__pb2,
)


class MsgStub(object):
    """Msg defines the ibc/transfer Msg service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Transfer = channel.unary_unary(
                '/ibc.applications.transfer.v1.Msg/Transfer',
                request_serializer=ibc_dot_applications_dot_transfer_dot_v1_dot_tx__pb2.MsgTransfer.SerializeToString,
                response_deserializer=ibc_dot_applications_dot_transfer_dot_v1_dot_tx__pb2.MsgTransferResponse.FromString,
                )


class MsgServicer(object):
    """Msg defines the ibc/transfer Msg service.
    """

    def Transfer(self, request, context):
        """Transfer defines a rpc handler method for MsgTransfer.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MsgServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Transfer': grpc.unary_unary_rpc_method_handler(
                    servicer.Transfer,
                    request_deserializer=ibc_dot_applications_dot_transfer_dot_v1_dot_tx__pb2.MsgTransfer.FromString,
                    response_serializer=ibc_dot_applications_dot_transfer_dot_v1_dot_tx__pb2.MsgTransferResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ibc.applications.transfer.v1.Msg', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Msg(object):
    """Msg defines the ibc/transfer Msg service.
    """

    @staticmethod
    def Transfer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ibc.applications.transfer.v1.Msg/Transfer',
            ibc_dot_applications_dot_transfer_dot_v1_dot_tx__pb2.MsgTransfer.SerializeToString,
            ibc_dot_applications_dot_transfer_dot_v1_dot_tx__pb2.MsgTransferResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
