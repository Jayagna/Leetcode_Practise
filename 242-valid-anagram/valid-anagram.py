class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1=defaultdict(int)
        d2=defaultdict(int)

        for i in s:
            d1[i]+=1
        for j in t:
            d2[j]+=1
        
        return True if d1==d2 else False