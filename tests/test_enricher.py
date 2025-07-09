 
# tests/test_enricher.py

import unittest
import pandas as pd
from steeleye_assignment.enricher import DataEnricher

class TestDataEnricher(unittest.TestCase):
    def setUp(self):
        data = {
            "FinInstrmGnlAttrbts.FullNm": ["Alpha Asset", "Beta Fund", "ZXY"],
        }
        self.df = pd.DataFrame(data)

    def test_enrich(self):
        enricher = DataEnricher(self.df)
        enriched_df = enricher.enrich()

        self.assertIn("a_count", enriched_df.columns)
        self.assertIn("contains_a", enriched_df.columns)

        self.assertEqual(enriched_df.loc[0, "a_count"], 3)  # "Alpha Asset"
        self.assertEqual(enriched_df.loc[0, "contains_a"], "YES")

        self.assertEqual(enriched_df.loc[2, "a_count"], 0)
        self.assertEqual(enriched_df.loc[2, "contains_a"], "NO")
