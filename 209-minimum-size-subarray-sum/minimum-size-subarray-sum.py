class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        res = 0
        minl = float('inf')

        for r in range(len(nums)):
            res += nums[r]

            while res >=  target:
                minl = min(minl, r - l + 1)
                res -= nums[l]
                l += 1

        return 0 if minl == float('inf') else minl
        