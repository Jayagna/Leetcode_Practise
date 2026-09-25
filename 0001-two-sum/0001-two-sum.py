class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        res = {}

        for i,val in enumerate(nums):
            if target - val in res:
                return [res[target-val],i]
            res[val] = i