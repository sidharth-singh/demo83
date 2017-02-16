import socket

host="www.google.co.in"
port=80

conn=socket.socket()

socket.send(str.encode("GET / HTTP/1.1\rl\nHost: google.co.in\r\n\r\n"))

response= socket.recv(2048)
print("Response recieved from: ")
print(str(response, "utf-8"))

