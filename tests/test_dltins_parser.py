# tests/test_dltins_parser.py

import unittest
from steeleye_assignment.dltins_parser import DLTINSParser

class TestDLTINSParser(unittest.TestCase):
    def setUp(self):
        self.xml_path = "extracted/DLTINS_20210119_01of02.xml"  # adjust if needed

    def test_parse_to_dataframe(self):
        parser = DLTINSParser(self.xml_path)
        df = parser.parse_to_dataframe()

        self.assertIsNotNone(df)
        self.assertFalse(df.empty)

        expected_columns = [
            "FinInstrmGnlAttrbts.Id",
            "FinInstrmGnlAttrbts.FullNm",
            "FinInstrmGnlAttrbts.ClssfctnTp",
            "FinInstrmGnlAttrbts.CmmdtyDerivInd",
            "FinInstrmGnlAttrbts.NtnlCcy",
            "Issr"
        ]
        for col in expected_columns:
            self.assertIn(col, df.columns)
 
