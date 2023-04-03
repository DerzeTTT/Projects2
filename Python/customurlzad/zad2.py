import socket

tUrl = 'httpbin.org'

newSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
newSock.connect((tUrl, 80))

headers = {

    'HOST':'httpbin.org',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'

}

appending = f"GET /html\r\n"

for i,v in headers.items():

    appending += f"{i}: {v}\r\n"

appending += "\r\n"

newSock.sendall(appending.encode())
response = newSock.recv(5000)

newFile = open("binhtml.html", "w")
newFile.write(response.decode())

newFile.close()