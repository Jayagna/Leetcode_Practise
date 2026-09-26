class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        freq = {}

        for num in nums:
            freq[num] = 1 + freq.get(num,0)

            if len(freq) == 2:
                for k in list(freq.keys()):
                    freq[k] -= 1
                    if freq[k] == 0:
                        del freq[k]

        return list(freq.keys())[0]