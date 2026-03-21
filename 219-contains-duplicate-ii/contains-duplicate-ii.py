class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        cmap = {}  # value -> last index

        for i, v in enumerate(nums):
            if v in cmap:
                if i - cmap[v] <= k:
                    return True
            cmap[v] = i  # update last seen index

        return False
        