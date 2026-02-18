class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        times = int(len(nums)/3)
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num,0)

        res = []
        for k,v in count.items() : 
            if v > times:
                res.append(k)

        return res    
        