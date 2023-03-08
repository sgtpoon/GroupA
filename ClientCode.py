# Importing the relevant libraries to execute the server side code.
# The socket library is used to connect the client to the server.
# The pickle module is used to serealise and deserealise objects.
# The json module is being imported in case the client decides to
# serealise the data in this format. The cElementree module is used
# for the file the client sends to the server.

import socket
import pickle
import json
import xml.etree.cElementTree as ElTree

# Declaring the local host and port variables that the Server
# will be attempting to detect.

LocHost = "localhost"
LocPort = 5555

# Creating a socket object from the client side.
cli_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecting to the server call we processed earlier.
cli_socket.connect((LocHost, LocPort))

# Creating Dictionary as per project specifications
Dict = {"Project Manager": "Timothy Poon",
        "Software Engineer": "Saad Syed",
        "Software Test": "Timothy Poon",
        "Software Architect": "Saad Syed"
        }
