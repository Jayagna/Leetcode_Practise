class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        hset = set(nums)
        out = 0

        for num in hset:
            if (num - 1) not in hset:
                length = 1
                while (num +  length) in hset:
                    length += 1
                out = max(length,out)
        return out