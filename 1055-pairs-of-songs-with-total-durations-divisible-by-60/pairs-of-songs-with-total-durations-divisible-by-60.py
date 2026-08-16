class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        freq = [0] * 60
        ans = 0

        for duration in time:

            rem = duration % 60
            need = (60 - rem) % 60

            ans += freq[need]

            freq[rem] += 1

        return ans

