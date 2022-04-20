import socket
import nacl.utils

def rand():
    buf = nacl.utils.random(128)
    for i in buf:
        print(hex(i)[2:], end = " ")
    
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Reuse port
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

# Bind the socket to the port
server_address = ('127.0.0.1', 55555)

print('Empezando en {} Puerto {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('Esperando una conexion')
    connection, client_address = sock.accept()
    try:
        print('Conexion desde', client_address)
        
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print('Se recibió {!r}'.format(data))
            rand()
            print('\nEnviando de regreso al cliente', format(data))
            connection.sendall(data)

    finally:
        # Clean up the connection
        connection.close()