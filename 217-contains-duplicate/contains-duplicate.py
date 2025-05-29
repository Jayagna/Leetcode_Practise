class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        se = set()
        for i in nums:
            if i in se:
                return True
            else:
                se.add(i)
        return False
       