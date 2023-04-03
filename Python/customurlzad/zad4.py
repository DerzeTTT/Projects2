import socket

newSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
newSocket.connect(('httpbin.org', 80))

data = 'comments=test123&custemail=ok@gmail.com&custname=fwasad&custtel=5325242532&delivery=11:15&size=small&topping=bacon'
request = "POST /post HTTP/1.1\r\nHost: httpbin.org\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: {}\r\n\r\n{}".format(len(data), data)

newSocket.send(request.encode())

response = newSocket.recv(4096)

print(response.decode())

newSocket.close()
