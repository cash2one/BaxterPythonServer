from unittest import TestCase

from Server import Server
from customexceptions.CustomExceptions import ServerNotStartedException
from mock import MagicMock


class TestServer(TestCase):

    def setUp(self):
        self.server = Server()

    def tearDown(self):
        self.server.close_connection()

    def test_StartListeningWithConnectionParameters_isConnectedTrue(self):
        self.server.start_listening("localhost", 1313)
        result = self.server.is_listening()
        TestCase.assertEqual(self, result, True)

    def test_StartListeningWithoutConnectionParameters_isConnectedTrue(self):
        self.assertRaises(ServerNotStartedException, self.server.start_listening, "129.122.2.1", 1314)

    def test_Run_AcceptConnection_Connected(self):
        self.server.accept_new_connection = MagicMock(return_value=False)
        self.server.run()
        self.assertEqual(0, self.server.is_listening())

    def test_ProcessReceivedData(self):
        self.server.process_received_data("Test")




