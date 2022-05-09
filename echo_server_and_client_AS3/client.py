import socket
import struct
from random import randint

HOST = '127.0.0.1'
PORT = 8899

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# input how many times client send request
times = input('Echo send: ')

id = randint(1, 65536)
for seq in range(times):

    out_data = struct.pack("!BBHHH9s3x", 8, 0, 65535, id, seq+1, b'108703014')
    
    # print and send data
    print(b"send:" + out_data)
    s.send(out_data)

    # revcieve and print data
    in_data = s.recv(20)
    print(b"recv: " + in_data)

    seq += 1

# after send and recieve data, close socket
s.close()