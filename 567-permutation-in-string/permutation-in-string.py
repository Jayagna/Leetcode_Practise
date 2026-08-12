class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = [0]*26

        if len(s1) > len(s2):
            return False
        
        for s in s1:
            freq1[ord(s)-ord('a')] += 1
        
        for s in range(len(s2)-len(s1)+1):
            freq2 = [0]*26
            for j in range(s,s+len(s1)):
                freq2[ord(s2[j])-ord('a')] += 1

            if freq1 == freq2:
                return True
        return False