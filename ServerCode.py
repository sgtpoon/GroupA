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
