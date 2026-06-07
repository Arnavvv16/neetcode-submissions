class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(0,32):
            k = n >> i & 1
            res += (k <<(31-i) )   
        return res