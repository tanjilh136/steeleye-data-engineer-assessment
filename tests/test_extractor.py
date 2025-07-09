# tests/test_extractor.py

import os
import unittest
from steeleye_assignment.extractor import Extractor

class TestExtractor(unittest.TestCase):
    def setUp(self):
        self.extractor = Extractor(extract_dir="test_extracted")
        self.zip_path = "downloads/DLTINS_20210119_01of02.zip"

    def test_extract_xml_file(self):
        xml_path = self.extractor.extract_xml(self.zip_path)
        self.assertIsNotNone(xml_path)
        self.assertTrue(xml_path.endswith(".xml"))
        self.assertTrue(os.path.exists(xml_path))

    def tearDown(self):
        # Clean up extracted files
        for file in os.listdir("test_extracted"):
            os.remove(os.path.join("test_extracted", file))
        os.rmdir("test_extracted")
 
