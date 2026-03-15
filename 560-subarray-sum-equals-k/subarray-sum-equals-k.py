class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0 
        prefixfreq = defaultdict(int)
        prefixfreq[0] = 1
        sum = 0
        for n in nums:
            sum += n
            if (sum - k) in prefixfreq:
                res += prefixfreq[sum-k]
            prefixfreq[sum] += 1
        return res
        