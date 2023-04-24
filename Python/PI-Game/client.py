import socket as s
import json

serverData = json.load(open('server-data.json'))

newSocket = s.socket(s.AF_INET, s.SOCK_STREAM)
newSocket.connect((serverData['IP'], serverData['Port']))

while True:

    guessInput = input('Guess from 1-100:\n')

    if int(guessInput) > 100 or int(guessInput) < 1:

        print("Include number within range")
        continue

    newSocket.sendall(guessInput.encode())
    received = newSocket.recv(512).decode()

    print(received)

    if received == 'Correct':

        break

print("Closing connection")