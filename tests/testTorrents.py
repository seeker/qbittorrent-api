import unittest
import time
from qbittorrentapi import Client


class TorrentTests(unittest.TestCase):
    def setUp(self):
        self.zero_torrent_hash = 'df13453e099eb4ca5329bb95d834e00edb93e232'

        self.client = Client(host='192.168.42.10:8080', VERIFY_WEBUI_CERTIFICATE=False)
        self.client.auth_log_in('vagrant_test', '12345678')

        self.client.torrents.add(torrent_files='./torrents/zero.torrent')

        torrent_info = self.client.torrents.info(hashes=[self.zero_torrent_hash])
        while torrent_info[0].state == 'checkingResumeData':
            time.sleep(0.2)
            torrent_info = self.client.torrents.info(hashes=[self.zero_torrent_hash])

    def tearDown(self):
        # TODO document that deleteFiles is required, the error message (missing param) is not helpful
        self.client.torrents.delete.all(deleteFiles=False)

    def test_add_torrent(self):
        torrent_info = self.client.torrents.info(hashes=[self.zero_torrent_hash])

        self.assertEqual(1, len(torrent_info))

    def test_recheck_torrent(self):
        self.client.torrents.recheck(hashes=[self.zero_torrent_hash])
        time.sleep(2)

        torrent_info = self.client.torrents.info(hashes=[self.zero_torrent_hash])

        self.assertEqual(0.5, torrent_info[0].progress)

    def test_pause_torrent(self):
        self.client.torrents.pause(hashes=[self.zero_torrent_hash])

        time.sleep(2)
        torrent_info = self.client.torrents.info(hashes=[self.zero_torrent_hash])

        self.assertEqual('pausedDL', torrent_info[0].state)

    def test_torrent_contents(self):
        torrent_info = self.client.torrents.info(hashes=[self.zero_torrent_hash])

        self.assertEqual(torrent_info.data[0].files.data[0].name, 'zero')


if __name__ == '__main__':
    unittest.main()
