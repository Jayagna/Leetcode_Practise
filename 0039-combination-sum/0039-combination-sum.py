class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(arr,i):
            if arr and sum(arr) == target:
                res.append(arr.copy())
                return
            if sum(arr) > target or i == len(nums):
                return
            arr.append(nums[i])
            dfs(arr,i)
            arr.pop()
            dfs(arr,i+1)

        dfs([],0)

        return res