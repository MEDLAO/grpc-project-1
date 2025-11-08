import grpc
import math_pb2
import math_pb2_grpc


def run():
    # open a connection (channel) to the server's address:port
    channel = grpc.insecure_channel("localhost:50051")

    # create a client stub (interface) for the MathService
    stub = math_pb2_grpc.MathServiceStub(channel)

    # build the request message and call the remote RPC
    # resp = stub.Square(math_pb2.SquareRequest(number=7))
    resp = stub.Cube(math_pb2.SquareRequest(number=3))
    # use the result (demo)
    print(resp.result)


if __name__ == "__main__":
    run()
