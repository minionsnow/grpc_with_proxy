# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import Calc_pb2 as Calc__pb2


class CalculatorStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Add = channel.unary_unary(
                '/calc.Calculator/Add',
                request_serializer=Calc__pb2.AddRequest.SerializeToString,
                response_deserializer=Calc__pb2.AddReply.FromString,
                )
        self.Substract = channel.unary_unary(
                '/calc.Calculator/Substract',
                request_serializer=Calc__pb2.SubstractRequest.SerializeToString,
                response_deserializer=Calc__pb2.SubstractReply.FromString,
                )
        self.Multiply = channel.unary_unary(
                '/calc.Calculator/Multiply',
                request_serializer=Calc__pb2.MultiplyRequest.SerializeToString,
                response_deserializer=Calc__pb2.MultiplyReply.FromString,
                )
        self.Divide = channel.unary_unary(
                '/calc.Calculator/Divide',
                request_serializer=Calc__pb2.DivideRequest.SerializeToString,
                response_deserializer=Calc__pb2.DivideReply.FromString,
                )


class CalculatorServicer(object):
    """Missing associated documentation comment in .proto file"""

    def Add(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Substract(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Multiply(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Divide(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CalculatorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Add': grpc.unary_unary_rpc_method_handler(
                    servicer.Add,
                    request_deserializer=Calc__pb2.AddRequest.FromString,
                    response_serializer=Calc__pb2.AddReply.SerializeToString,
            ),
            'Substract': grpc.unary_unary_rpc_method_handler(
                    servicer.Substract,
                    request_deserializer=Calc__pb2.SubstractRequest.FromString,
                    response_serializer=Calc__pb2.SubstractReply.SerializeToString,
            ),
            'Multiply': grpc.unary_unary_rpc_method_handler(
                    servicer.Multiply,
                    request_deserializer=Calc__pb2.MultiplyRequest.FromString,
                    response_serializer=Calc__pb2.MultiplyReply.SerializeToString,
            ),
            'Divide': grpc.unary_unary_rpc_method_handler(
                    servicer.Divide,
                    request_deserializer=Calc__pb2.DivideRequest.FromString,
                    response_serializer=Calc__pb2.DivideReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'calc.Calculator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Calculator(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def Add(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/calc.Calculator/Add',
            Calc__pb2.AddRequest.SerializeToString,
            Calc__pb2.AddReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Substract(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/calc.Calculator/Substract',
            Calc__pb2.SubstractRequest.SerializeToString,
            Calc__pb2.SubstractReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Multiply(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/calc.Calculator/Multiply',
            Calc__pb2.MultiplyRequest.SerializeToString,
            Calc__pb2.MultiplyReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Divide(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/calc.Calculator/Divide',
            Calc__pb2.DivideRequest.SerializeToString,
            Calc__pb2.DivideReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)