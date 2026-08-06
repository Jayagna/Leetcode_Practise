class Solution:
    def beautySum(self, s: str) -> int:
        tot = 0
        for i in range(len(s)):
            freq = [0]*26
            for j in range(i,len(s)):
                freq[ord(s[j])-ord('a')] += 1

                tot += max(freq) - min(count for count in freq if count>0)

        return tot
