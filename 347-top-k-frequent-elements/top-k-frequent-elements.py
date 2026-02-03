class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        countmap = {}
        output = []
        for i in nums:
            if i in countmap:
                countmap[i] += 1
            else:
                countmap[i] = 1
        for i in range(k):
            max_freq, max_key = 0,0
            for key in countmap:
                if (countmap[key] > max_freq):
                    max_freq = countmap[key]
                    max_key = key
            output.append(max_key)
            del countmap[max_key]
        return output      