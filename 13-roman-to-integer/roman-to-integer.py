class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000} 
        tot = dic[s[-1]]

        for i in range(len(s)):
            if i + 1 < len(s):
                if dic[s[i+1]] > dic[s[i]]:
                    tot -= dic[s[i]]
                else:
                    tot += dic[s[i]]

        return tot