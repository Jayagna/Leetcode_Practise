class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        i = 0
        while n >= 1:
            if 1 & n != 0:
                cnt += 1
            n >>= 1
        return cnt