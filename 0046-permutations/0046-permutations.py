class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        taken = [False]*len(nums)

        def dfs(arr):
            if len(nums) == len(arr):
                res.append(arr.copy())
                return
            
            

            for i in range(len(nums)):
                if taken[i] != True:
                    taken[i] = True
                    arr.append(nums[i])
                    dfs(arr)
                    arr.pop()
                    taken[i] = False

        dfs([])

        return res