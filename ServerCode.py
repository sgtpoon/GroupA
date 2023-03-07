# Importing the relevant libraries to execute the server side code.
# The socket library is used to connect the client to the server.
# The pickle module is used to serealise and deserealise objects.
# The json module is being imported in case the client decides to
# serealise the data in this format. The cElementree module is used
# for the file the client sends to the server. The os module will
# be used for the code to interact with the operating system.

import socket
import pickle
import json
import xml.etree.cElementTree as ElTree
import os

# Declaring the local host and port variables that the Server
# will be attempting to detect. FileLog enables the content
# to be printed onto a file per the project specification.
# The encryption key will be used to to encrypt the dict.

LocHost = "localhost"
LocPort = 5555
FileLog = "File_log.txt"
Encrypt_key = b"password"

# Establish a socket object (i.e. a communication end point)
ser_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Next we make a connecting between the network socket with
# a local network address and port number.
ser_socket.bind((LocHost, LocPort))

# Next, we enable the server to detect incoming connections.
ser_socket.listen()
print(
    f"Server is actively listening on [Host: {LocHost}] and [Port:{LocPort}]")

while True:
    # Connecting to a client call
    cli_socket, cli_address = ser_socket.accept()
    print(f"Connection has been established with {cli_address}")

    # close connection with client
    cli_socket.close()
