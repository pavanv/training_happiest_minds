#!/usr/bin/python           # This is server.py file

import socket               # Import socket module

def server():
    s = socket.socket()         # Create a socket object
    host = socket.gethostname() # Get local machine name
    port = 12345                # Reserve a port for your service.
    s.bind((host, port))        # Bind to the port

    s.listen(5)                 # Now wait for client connection.
    print 'Listening for connections on port {}'.format(port)
    while True:
        conn, addr = s.accept()     # Establish connection with client.
        print 'Got connection from', addr
        conn.send('Thank you for connecting')
        conn.close()                # Close the connection

if __name__ == '__main__':
    server()