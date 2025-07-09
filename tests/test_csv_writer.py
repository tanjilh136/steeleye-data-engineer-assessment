# tests/test_csv_writer.py

import os
import unittest
import pandas as pd
from steeleye_assignment.csv_writer import CSVWriter

class TestCSVWriter(unittest.TestCase):
    def setUp(self):
        self.output_dir = "test_output"
        self.filename = "test_dltins.csv"
        self.writer = CSVWriter(output_dir=self.output_dir)

        # Sample DataFrame
        self.df = pd.DataFrame({
            "Id": ["AAA", "BBB"],
            "Name": ["Test A", "Test B"],
            "a_count": [1, 0],
            "contains_a": ["YES", "NO"]
        })

    def test_save_to_csv(self):
        output_path = self.writer.save_to_csv(self.df, filename=self.filename)
        self.assertTrue(os.path.exists(output_path))

        # Check contents (optional)
        saved_df = pd.read_csv(output_path)
        self.assertEqual(saved_df.shape, self.df.shape)
        self.assertListEqual(saved_df.columns.tolist(), self.df.columns.tolist())

    def tearDown(self):
        # Clean up output directory
        file_path = os.path.join(self.output_dir, self.filename)
        if os.path.exists(file_path):
            os.remove(file_path)
        if os.path.exists(self.output_dir):
            os.rmdir(self.output_dir)
 
