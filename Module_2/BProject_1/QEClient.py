import grpc

# After getting to the correct directory with the path to our .proto file
# I used this command (from the video found in Mod 2) to auto generate the files for
# our QECalculator. 

# python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. QECalculator.proto

# Now we import the generated classes
import QECalculator_pb2
import QECalculator_pb2_grpc
import QECalculator

# Open a channel
channel = grpc.insecure_channel("localhost:50053")

# Create a stub (client)
stub = QECalculator_pb2_grpc.QEcalculatorStub(channel)

# Getting user input for the variables in the equation
a = float(input("Enter the value for a: "))
b = float(input("Enter the value for b: "))
c = float(input("Enter the value for c: "))

# Creating a valid request message
request = QECalculator_pb2.QEvar(a = a, b = b, c = c)

# Making response call
response = stub.Calculate(request)

# Printing the answer
if response.ans:
    for i in response.ans:
        print(f"The answer to the quadratic equation provided is: ", i)
else:
    print("There are no real square roots.")

