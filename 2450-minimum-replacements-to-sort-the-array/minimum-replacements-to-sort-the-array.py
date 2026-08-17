class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans = 0
        allowed = nums[-1]

        for i in range(len(nums)-2,-1,-1):
            current = nums[i]
            if current <= allowed:
                allowed = current
            else:
                pieces = math.ceil(current/allowed)
                ans += pieces - 1
                allowed = current//pieces

        return ans