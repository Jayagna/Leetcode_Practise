class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(1,len(nums)):
            j = i
            while(j!=0 and nums[j] <  nums[j-1]):
                temp = nums[j]
                nums[j] = nums[j-1]
                nums[j-1] = temp
                j -= 1 
        return nums
        