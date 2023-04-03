import socket

tUrl = 'httpbin.org'

newSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
newSock.connect((tUrl, 80))

headers = {

    'HOST':'httpbin.org',
}

appending = f"GET /image/png \r\n"

for i,v in headers.items():

    appending += f"{i}: {v}\r\n"

appending += "\r\n"

newSock.sendall(appending.encode())
response = newSock.recv(10000)

newFile = open("extractedimage.png", "wb")
newFile.write(response)

newFile.close()