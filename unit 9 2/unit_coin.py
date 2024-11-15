import unittest
import io
from coin import *

class TestCoin(unittest.TestCase):
    #unit test for init
    def test_init(self):
        coin = GVCoin(5)
        self.assertEqual(coin.num_flips(), 0)
        self.assertEqual(coin.num_heads(), 0)
        self.assertEqual(coin.num_tails(), 0)
        self.assertEqual(coin.get_is_heads(), True)

    #unit test For testing if the coin is balanced and gives a statistically significant number of heads and tails that is matched for a reasonable sample size
    def test_balanced(self):
        coin = GVCoin(5)
        print("I'm runnning!")
        for i in range(1000):
            coin.flip()
        self.assertTrue(coin.num_heads() > 450)
        self.assertTrue(coin.num_tails() > 450)

    #unit test for flip
    def test_flip(self):
        coin = GVCoin(5)
        coin.flip()
        self.assertEqual(coin.num_flips(), 1)
        self.assertEqual(coin.num_heads(), 1)
        self.assertEqual(coin.num_tails(), 0)

    #unit test for consecutive_heads
    def test_consecutive_heads(self):
        coin = GVCoin(5)
        self.assertEqual(consecutive_heads(coin, 5), 57)

    
if __name__ == '__main__':
    unittest.main()