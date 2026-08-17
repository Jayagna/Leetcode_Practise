class Solution:
    def minOperations(self, n: int) -> int:
        ops = 0

        while n > 0:
            lowbit = n & -n
            if n & (lowbit<<1):
                n += lowbit
            else:
                n -= lowbit
            ops += 1

        return ops
