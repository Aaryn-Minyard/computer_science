import unittest
from unittest.mock import patch
from art import Artist, Artwork

class TestArtwork(unittest.TestCase):

    def setUp(self):
        self.artist_tier1 = Artist("Leonardo da Vinci", 1452, 1519)
        self.artist_tier2 = Artist("Claude Monet", 1840, 1926)
        self.artist_tier3 = Artist("Gustav Klimt", 1862, 1918)
        self.artist_other = Artist("Unknown Artist", 1900, 1980)
        self.artist_other2 = Artist("Aaryn Minyard", 2001, 2101)

    def test_price_tier1(self):
        artwork = Artwork("Mona Lisa", 1503, self.artist_tier1)
        self.assertEqual(artwork.price(), "$38,656,716.42")

    def test_price_tier2(self):
        artwork = Artwork("Water Lilies", 1916, self.artist_tier2)
        self.assertEqual(artwork.price(), "$1,220,930.23")

    def test_price_tier3(self):
        artwork = Artwork("The Kiss", 1908, self.artist_tier3)
        self.assertEqual(artwork.price(), "$807,142.86")

    def test_price_other(self):
        artwork = Artwork("Unknown Artwork", 1950, self.artist_other)
        self.assertEqual(artwork.price(), "$10,952.25")

    def test_price_future(self):
        artwork = Artwork("Future Artwork", 2025, self.artist_other)
        self.assertEqual(artwork.price(), "$624,123.82")

    def test_print_info(self):
        artwork = Artwork("Mona Lisa", 1503, self.artist_tier1)

        with patch('builtins.print') as mocked_print:
            artwork.print_info()
            mocked_print.assert_any_call('"Mona Lisa" was created by Leonardo da Vinci in 1503.')
            mocked_print.assert_any_call('Leonardo da Vinci was born in 1452 and died in 1519.')
            mocked_print.assert_any_call('This artwork is worth $38,656,716.32')
            

if __name__ == '__main__':
    unittest.main()