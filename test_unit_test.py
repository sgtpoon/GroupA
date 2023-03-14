import socket
import unittest
import pickle


class TestServer(unittest.TestCase):
    # The following is a multipronged unit test to check that
    # the connection between the client and server is made and
    # that the server is able to receive and manipulate data.
    def test_check_server_working(self):
        LocHost = "localhost"
        LocPort = 5555
        ser_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ser_socket.bind((LocHost, LocPort))
        ser_socket.listen()

        cli_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cli_socket.connect((LocHost, LocPort))

        dict_data = {"PM": "Timothy Poon", "Engineer": "Saad"}
        dict_serialised = pickle.dumps(
            dict_data, protocol=pickle.DEFAULT_PROTOCOL)

        cli_socket.sendall(dict_serialised)
        cli_socket.close()

        cli_socket, cli_address = ser_socket.accept()
        dict_recv = cli_socket.recv(4096)
        ReceivedData = pickle.loads(dict_recv)
        self.assertEqual(ReceivedData, dict_data)
        cli_socket.close()

        ser_socket.close()


if __name__ == '__main__':
    unittest.main()
