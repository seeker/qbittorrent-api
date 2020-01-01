import unittest
from qbittorrentapi import Client

class ApplicationTests(unittest.TestCase):
    def setUp(self):
        self.client = Client(host='192.168.42.10:8080', VERIFY_WEBUI_CERTIFICATE=False)
        self.client.auth_log_in('vagrant_test', '12345678')

    def test_login(self):
        self.assertEqual(self.client.application.version, 'v4.2.1')

if __name__ == '__main__':
    unittest.main()
