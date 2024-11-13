import random

class GVCoin :
    def __init__(self, seed):
        random.seed(seed)
        self._is_heads = True
        self.heads = 0
        self.flips = 0

    def num_flips(self):
        return self.flips

    def num_heads(self):
        return self.heads

    def num_tails(self):
        return self.flips - self.heads

    def flip(self):
        self.is_heads = random.randint(0, 1)
        self.flips += 1
        if self.is_heads == 1:
            self.heads += 1

    def get_is_heads(self):
        return self.is_heads

def consecutive_heads(gv_coin, goal):
    count = 0
    while count < goal:
        gv_coin.flip()
        if gv_coin.get_is_heads() == 1:
            count += 1
        else:
            count = 0
    return gv_coin.num_flips()

    # Type your code here

if __name__ == "__main__":
    gv_coin = GVCoin(15)
    num_heads = 5
    num_flips = consecutive_heads(gv_coin, num_heads)
    print(f'Total number of flips for 5 consecutive heads: { num_flips }')