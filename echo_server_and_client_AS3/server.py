import socket
import threading
import struct

s = socket.socket()
HOST = '127.0.0.1'
PORT = 8899

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(5)
print("Server running on port ", PORT)

def serveClient(clientsocket, address):
    
    # we need a loop to continuously receive messages from the client
    while True:
        # then receive at most 1024 bytes message and store these bytes in a variable named 'data'
        # you can set the buffer size to any value you like
        in_data = clientsocket.recv(20)
        
        if in_data == '':
            continue

        print("client data: ", in_data)

        # if the received data is not empty, then we send something back by using send() function
        type, code, unused, id, seq, message= struct.unpack("!BBHHH9s3x", in_data)
        out_data = struct.pack("!BBHHH9s3x", 0, code, unused, id, seq, message)

        if in_data:
            print("sent data: ", in_data)
            clientsocket.send(out_data)

while True:
    # accept a new client and get it's information
    (clientsocket, address) = s.accept()
    
    # create a new thread to serve this new client
    # after the thread is created, it will start to execute 'target' function with arguments 'args' 
    threading.Thread(target = serveClient, args = (clientsocket, address)).start()