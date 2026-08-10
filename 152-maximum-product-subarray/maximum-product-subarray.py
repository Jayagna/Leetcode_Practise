class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cmax,cmin = 1,1
        res = max(nums)

        for i in range(len(nums)):
            tmp = cmax
            cmax = max(nums[i]*cmax,nums[i]*cmin,nums[i])
            cmin = min(nums[i]*tmp,nums[i]*cmin,nums[i])

            res = max(cmax,res)
        
        return res