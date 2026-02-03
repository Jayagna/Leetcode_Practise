class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = 0
        for j in range(2):
            for i in range(len(nums)):
                if (nums[i] == j):
                    nums[i],nums[l] = nums[l],nums[i]
                    l += 1
        return nums
        