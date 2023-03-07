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
# will be attempting to detect. FileLog enables the content
# to be printed onto a file per the project specification.
# The encryption key will be used to to encrypt the dict.

LocHost = "localhost"
LocPort = 5555
