#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
from thread import start_new_thread

def clientthread(conn):
    conn.send('Thank you for connecting')
    conn.close()                # Close the connection

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

        #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
        start_new_thread(clientthread ,(conn,))

if __name__ == '__main__':
    server()