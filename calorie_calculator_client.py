import zmq
import time
import os

clear = lambda: os.system('clear')

context = zmq.Context()

print("Connecting to Calorie Calculator...")
time.sleep(5)
clear()

socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:6666")

requests = ["calorie_calculator-2023-02-08.txt gender",
            "calorie_calculator-2023-02-08.txt weight",
            "calorie_calculator-2023-02-08.txt height",
            "calorie_calculator-2023-02-08.txt age",
            "calorie_calculator-2023-02-08.txt activity",
            "calorie_calculator-2023-02-08.txt calories"]
for request in requests:
    print(f"Sending request '{request}'...")
    socket.send_string(request)

    message = socket.recv()
    message = message.decode('UTF-8')
    history = message.split(',')
    print()
    print(f"Your calorie calculation history: ")
    for variable in history:
        print(variable)
    print("--------------------------------")
