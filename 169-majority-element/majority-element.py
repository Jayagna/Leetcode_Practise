class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for num in nums:
                count[num] = 1 + count.get(num,0)
        for k,v in count.items():
            if v > len(nums)/2:
                return k