class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for n in nums:
            if n == val:
                count += 1
            
        for i in range(count):
            nums.remove(val)