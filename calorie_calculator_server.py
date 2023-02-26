# Name: Maggie Wu
# Github UN: wumag
# Date: 02/14/2023
# Description: Server code to receive data

import zmq
import time
import os

# Create a ZeroMQ context object and socket object, and bind to port 6666
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:6666")

# Read the path from the request.txt file, and read the contents of the file into a list
with open('request.txt', 'r') as f:
    path = f.read().strip()
with open(path, 'r') as f:
    history = [line.strip() for line in f]

# Define a lambda function that clears the console
clear = lambda: os.system('clear')

# Print a message indicating connection to Calorie Calculator and clear the console after a 5 second delay
print("Connecting to Calorie Calculator...")
time.sleep(5)
clear()

# Define a function to handle incoming requests
def main():
    while True:
        msg = socket.recv()
        print("Waiting for request from client...")
        print(f"Request received: {msg}")

        # Decode the message and split it into separate parts
        msg = msg.decode('UTF-8')
        params = msg.split(' ')
        variable = str(params[1])

        # Determine which element of the history list to send back to the client based on the requested variable
        if variable == 'gender':
            i = 0
        
        if variable == 'weight':
            i = 1

        if variable == 'height':
            i = 2

        if variable == 'age':
            i = 3  

        if variable == 'activity':
            i = 4

        if variable == 'calories':
            i = 5

        # Send the requested element of the history list back to the client
        socket.send_string(history[i])
        print("Response sent to client!")
        print("--------------------------------")

if __name__ == '__main__':
    main()
