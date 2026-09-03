class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        res = [False]*(len(nums)+1)

        for val in nums:
            if val > 0 and val < len(nums) + 1:
                res[val] = True

        for i in range(1,len(res)):
            if res[i] == False:
                return i

        return len(nums) + 1