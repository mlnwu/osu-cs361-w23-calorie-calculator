# Name: Maggie Wu
# Github UN: wumag
# Date: 02/14/2023
# Description: Server code to receive data

import zmq
import time
import os

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:6666")

# Read the path from the request.txt file
with open('request.txt', 'r') as f:
    path = f.read().strip()

# Open the calorie-calculator-2023-02-08.txt file and read its contents line by line
with open(path, 'r') as f:
    history = [line.strip() for line in f]

clear = lambda: os.system('clear')

print("Connecting to Calorie Calculator...")
time.sleep(5)
clear()

def main():
    while True:
        msg = socket.recv()
        print("Waiting for request from client...")
        print(f"Request received: {msg}")

        msg = msg.decode('UTF-8')
        params = msg.split(' ')
        variable = str(params[1])

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

        socket.send_string(history[i])
        print("Response sent to client!")
        print("--------------------------------")

if __name__ == '__main__':
    main()
