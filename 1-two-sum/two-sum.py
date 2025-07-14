class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        for i in range(len(nums)):
            for j in range(len(nums)- i - 1):
                if nums[i] + nums[j+i+1] == target:
                    output.append(i)
                    output.append(j+i+1)
                    return output