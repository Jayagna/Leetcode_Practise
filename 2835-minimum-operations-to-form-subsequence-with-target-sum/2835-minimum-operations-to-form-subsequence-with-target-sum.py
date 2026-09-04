class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        if sum(nums) < target:
            return -1

        ops = 0
        count = defaultdict(int)
        for num in nums:
            count[num.bit_length()-1] += 1

        for i in range(31):
            if target & (1<<i):
                if count[i] > 0:
                    count[i] -= 1
                else:
                    j = i+1
                    while j < 32 and count[j] == 0:
                        j += 1
                    while j > i:
                        count[j] -= 1
                        count[j-1] += 2
                        ops += 1
                        j -= 1

                    count[i] -= 1

            count[i+1] += count[i]//2

        return ops