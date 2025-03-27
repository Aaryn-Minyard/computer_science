import os
import tempfile
import unittest
from tv_shows import process_tv_shows

class TestTVShowsProcessing(unittest.TestCase):
    def setUp(self):
        # Sample input data (as per the example)
        self.test_data = (
            "20\nGunsmoke\n"
            "30\nThe Simpsons\n"
            "10\nWill & Grace\n"
            "14\nDallas\n"
            "20\nLaw & Order\n"
            "12\nMurder, She Wrote\n"
        )
        # Create a temporary file with the test data
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, mode="w", suffix=".txt")
        self.temp_file.write(self.test_data)
        self.temp_file.close()

        # Ensure output files do not exist before the test
        for fname in ["output_keys.txt", "output_titles.txt"]:
            if os.path.exists(fname):
                os.remove(fname)

    def tearDown(self):
        # Clean up the temporary file and output files
        os.remove(self.temp_file.name)
        for fname in ["output_keys.txt", "output_titles.txt"]:
            if os.path.exists(fname):
                os.remove(fname)

    def test_process_tv_shows(self):
        # Run the processing function on the temporary file
        process_tv_shows(self.temp_file.name)
        
        # Test output_keys.txt
        self.assertTrue(os.path.exists("output_keys.txt"))
        with open("output_keys.txt", "r") as f:
            keys_content = f.read().strip()
        expected_keys = (
            "30: The Simpsons\n"
            "20: Gunsmoke; Law & Order\n"
            "14: Dallas\n"
            "12: Murder, She Wrote\n"
            "10: Will & Grace"
        )
        self.assertEqual(keys_content, expected_keys)

        # Test output_titles.txt
        self.assertTrue(os.path.exists("output_titles.txt"))
        with open("output_titles.txt", "r") as f:
            titles_content = f.read().strip()
        expected_titles = (
            "Will & Grace\n"
            "The Simpsons\n"
            "Murder, She Wrote\n"
            "Law & Order\n"
            "Gunsmoke\n"
            "Dallas"
        )
        self.assertEqual(titles_content, expected_titles)

if __name__ == '__main__':
    unittest.main()
