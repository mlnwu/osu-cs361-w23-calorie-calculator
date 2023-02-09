# Calorie Calculator
Calculate how many calories you should consume in a day to maintain your current weight!

## The Set Up
- Download calorie_calculator_microservice.py and run it in your preferred IDE
- Follow the prompts to create a local data file that will show up as: 'calorie-calculator-YYYY-MM-DD.txt'
- Ensure that you are using python3 in your preferred terminal with the command: `python --version`
- Install ZMQ with the command: `pip install zmq`

## How to Request Data
- Download calorie_calculator_client.py
- Requests can be sent in the form of '{nameoftextfile.txt} {variable}'
- Run the file in your terminal using the command: `python calorie_calculator_client.py`
- Example of what the calorie_calculator_client.py will look like:
```
Sending request 'calorie_calculator-2023-02-08.txt calories'...

Your calorie calculation history: 
You need to eat 2547.8250000000003 calories a day to maintain your current weight

```

## How to Receive Data
- Download calorie_calculator_server.py
- Variables must be 'gender', 'weight', 'height', 'age', 'activity', and/or 'calories'
- Run the file in your terminal using the command: `python calorie_calculator_server.py`
- Example of what the calorie_calculator_server.py will look like:
```
Waiting for request from client...
Request received: b'calorie_calculator-2023-02-08.txt calories'
Response sent to client!
```
## UML Sequence Diagram

![Screenshot 2023-02-09 at 12 32 32 AM](https://user-images.githubusercontent.com/107904188/217758678-50838e60-7e6c-4b82-b058-891a42d81806.png)
