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
dict = {"Project Manager: ": "Timothy Poon",
        "Software Engineer: ": "Saad Syed",
        "Software Testing: ": "Timothy Poon",
        "Software Architect: ": "Saad Syed"
        }

# The following block of code will allow the user to select the
# format as between JSON, binary, and XML. The user will select
# between numbers 1 to 3 from which. Thereafter, depending on the
# choice, we serialise the dictionary.

print("Please choose the required pickling format:")
print("1. Binary")
print("2. JSON")
print("3. XML")
select_format = int(input())
if select_format == 1:
    dict_serialised = pickle.dumps(dict, protocol=pickle.DEFAULT_PROTOCOL)
elif select_format == 2:
    dict_serialised = json.dumps(dict).encode("utf-8")
elif select_format == 3:
    root = ElTree.Element("dictionary")
    for pair, match in dict.items():
        elem = ElTree.SubElement(root, pair)
        elem.text = str(match)
    dict_serialised = ElTree.tostring(root)
else:
    print("Invalid option selected")
    exit()

# Next, we send the serealised dectionary to the server
cli_socket.sendall(dict_serialised)

# Next, we send the text file and send it to the server
with open("Send_Text_file.txt", "rb") as file:
    while True:
        file_info = file.read(5000)
        if not file_info:
            break
        cli_socket.sendall(file_info)

print("All items sent to server")

# close connection with the server
cli_socket.close()
