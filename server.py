import grpc
from concurrent import futures
import math_pb2
import math_pb2_grpc


# implements the MathService defined in the .proto file
class MathService(math_pb2_grpc.MathServiceServicer):
    def square(self, request, context):
        result_value = request.number * request.number
        return math_pb2.SquareResponse(result=result_value)


# function that starts and runs the gRPC server
def serve():
    # create gRPC server with thread pool (so it can handle multiple requests)
    server = grpc.server(futures.ThreadPoolExecutor())

    # register the MathService implementation to this gRPC server
    math_pb2_grpc.add_MathServiceServicer_to_server(MathService, server)

    # server will listen on port 50051 for incoming gRPC connections
    server.add_insecure_port("[::]:50051")

    server.start()
    server.wait_for_termination()  # keeps server running forever


if __name__ == "__main__":
    serve()
