import socket
import select
import sys


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP_address = socket.gethostbyname("")
Port = 9999
server.connect((IP_address, Port))

while True:

    # maintains a list of possible input streams
    sockets_list = [sys.stdin, server]

    read_sockets,write_socket, error_socket = select.select(sockets_list,[],sockets_list)
    for socks in read_sockets:
        if socks == server:
            message = str(socks.recv(2048),'utf-8')
            if "~exit~" in message:
                server.close()
                sys.exit()
            print(message)
            
        else:
            message = sys.stdin.readline()
            server.send(str.encode(message))
            sys.stdout.flush()
            """else:
                sys.exit()"""
server.close()
sys.exit()
