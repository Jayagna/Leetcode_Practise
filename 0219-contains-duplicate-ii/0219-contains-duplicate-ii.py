class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        cmap = {}

        
        for i, v in enumerate(nums):
            if v in cmap:
                if i - cmap[v] <= k:
                    return True
            cmap[v] = i  # update last seen index

        return False