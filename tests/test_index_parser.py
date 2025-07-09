# tests/test_index_parser.py

import unittest
from steeleye_assignment.index_parser import IndexParser

class TestIndexParser(unittest.TestCase):
    def test_second_dltins_url_extraction(self):
        parser = IndexParser("downloads/index.xml")  # You already have this file
        url = parser.get_second_dltins_url()
        self.assertIsNotNone(url)
        self.assertTrue(url.endswith(".zip"))
