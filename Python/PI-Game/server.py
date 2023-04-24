import socket as s
import random as ran
import json

serverData = json.load(open('server-data.json'))

def handleCon(tConn):

    corr = ran.randint(1,100)

    while True:

        data = tConn.recv(512)

        if not data: print("No data"); break

        guess = int(data.decode())

        if guess==corr:

            tConn.sendall(b'Correct')

        else:

            tConn.sendall((guess > corr and b'too high') or b'Too low')

newSocket = s.socket(s.AF_INET, s.SOCK_STREAM)

newSocket.bind((serverData['IP'], serverData['Port']))
newSocket.listen()

print('Server started')

while True:

    handleCon(newSocket.accept()[0])