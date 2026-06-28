class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hset = set()
        for num in nums:
            if num not in hset:
                hset.add(num)
            else:
                return num
        