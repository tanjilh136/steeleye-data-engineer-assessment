# tests/test_downloader.py

import os
import unittest
from steeleye_assignment.downloader import Downloader

class TestDownloader(unittest.TestCase):
    def setUp(self):
        self.downloader = Downloader(download_dir="test_downloads")

    def test_download_index_file(self):
        url = "https://registers.esma.europa.eu/solr/esma_registers_firds_files/select?q=*&fq=publication_date:[2021-01-17T00:00:00Z TO 2021-01-19T23:59:59Z]&wt=xml&indent=true&start=0&rows=100"
        file_path = self.downloader.download_file(url, "test_index.xml")
        self.assertTrue(os.path.exists(file_path))

    def tearDown(self):
        # Clean up test download directory
        for file in os.listdir("test_downloads"):
            os.remove(os.path.join("test_downloads", file))
        os.rmdir("test_downloads")
