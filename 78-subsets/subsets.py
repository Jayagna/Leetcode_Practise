class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(array,ind):
            if ind == len(nums):
                res.append(array.copy())
                return

            array.append(nums[ind])
            dfs(array,ind+1)
            array.pop()
            dfs(array,ind+1)

        dfs([],0)
        
        return res 