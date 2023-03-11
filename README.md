# End of Module Assginment

As part of this project, students were assigned to build a simple client/server network that creates a dictionary, populates it, serializes it and sends it to a server (along with a text file). Regarding the dictionary, the user should be able to set the pickling format to either binary, JSON and XML. Also, the user will need to have the option to encrypt the text in a text file. The server should have a configurable option to print the contents of the sent items to the screen and or to a file. 

## Systems Requirements

The following will be required in order to run the program:
1. Python 3.8 installed.
2. The pickle module.
3. The json module.
4. The xml.etree.ElementTree module. 
5. The socket module.

## Step 1 - Please run the Server file first

In order to run the Server file first, please run the command line from the Server file directory. Thereafter, please type the following command:

python ServerCode.py

This file will actively listen for incoming client calls and upon establishing a connection, it will receive:
- A Dictionary
- A Text File

The User will also be given the option for the contents of the files to be printed.

## Step 2 - Next, please run the Client file

In order to run the Client file, please run the command line from the Client file directory. Thereafter, please type the following command:

python ClientCode.py

Running the above command will enable the client to create a dictionary with some data and a choice of pickling format in order to serialise the data. The client is also able to send a text file to the server from this code.

## Project Contributors
1. Timothy Poon - Project Manager and Code Tester.
2. Saad Syed - Software Engineer and Software Architect.

## License

This assignment is licensed under MIT License.