class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        resolve,additions=0,0

        for i in range(len(s)):
            if s[i] == '(':
                resolve+=1
            else:
                if resolve>0:
                    resolve-=1
                else:
                    additions+=1

        return additions+resolve