# Importing all necessary elements
from concurrent import futures
import logging

import grpc
import QECalculator_pb2
import QECalculator_pb2_grpc
import QECalculator

# Creating a class to define server functions using the generated files
class QECalculatorServicer(QECalculator_pb2_grpc.QEcalculatorServicer):

    def Calculate(self, request, context):

        response = QECalculator_pb2.QEans()
        
        # Calling the quadratic function in my calculator to find the square roots of the equation
        sroots = QECalculator.quadratic(request.a, request.b, request.c)
        
        # If statement for no square roots
        if sroots is not None:

            # Case if there is more than one real square root
            if len(sroots) == 2:
                response.ans.extend(sroots)
            
            # Case if there is only one real square root
            else:
                response.ans.extend([sroots[0]])
        
        # Returning the response
        return response

        

    
def serve():

    # Create a grpc server
    port = 50053
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Add defined class to server
    QECalculator_pb2_grpc.add_QEcalculatorServicer_to_server(QECalculatorServicer(), server)

    # Listening on port 50051
    print("Starting server. Listening on port 50053.")
    server.add_insecure_port('[::]:' + str(port))
    server.start()
    print("Server started. Listening on " + str(port))
    server.wait_for_termination()

if __name__ == "__main__":
    logging.basicConfig()
    serve()