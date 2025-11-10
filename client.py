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
    # resp = stub.Cube(math_pb2.SquareRequest(number=3))
    # use the result (demo)
    # print(resp.result)

    try:
        # send a negative number to test server validation
        resp = stub.Sqrt(math_pb2.SquareRequest(number=-9))
        print(resp.result)  # gets printed only if NO error happens
    except grpc.RpcError as e:
        # this executes if server sends error
        print("Error:", e.code(), e.details())


if __name__ == "__main__":
    run()
