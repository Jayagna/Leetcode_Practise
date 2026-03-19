class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i+1,len(nums)-2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                l,r = j+1,len(nums)-1
                left = target - nums[i] - nums[j]
                
                while l<r:
                    tot = nums[l] + nums[r]
                    if tot > left:
                        r -= 1
                    elif tot < left:
                        l += 1
                    else : 
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        l += 1
                        r -= 1

                        while l<r and nums[l] == nums[l-1]:
                            l += 1
                        while l<r and nums[r] == nums[r+1]:
                            r -= 1
        return res
        