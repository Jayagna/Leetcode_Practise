class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        i = 0
        while i < len(nums)-2:
            target = -nums[i]
            j,k = i+1,len(nums)-1
            while j < k:
                if nums[j] + nums[k] == target:
                    res.append([nums[i],nums[j],nums[k]])
                    while j < len(nums) - 1 and nums[j+1] == nums[j]:
                        j += 1
                    j += 1
                    while k > 0 and nums[k] == nums[k-1]:
                        k -= 1
                    k -= 1
                elif nums[j] + nums[k] >= target:
                    while k > 0 and nums[k] == nums[k-1]:
                        k -= 1
                    k -= 1
                else:
                    while j < len(nums) - 1 and nums[j+1] == nums[j]:
                        j += 1
                    j += 1
            while i < len(nums) - 1 and nums[i] == nums[i+1]:
                i += 1
            i += 1

        return res