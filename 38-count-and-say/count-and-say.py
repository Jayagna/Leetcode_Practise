class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        
        s = self.countAndSay(n-1)

        left,right = 0,0
        count = 0
        result = []
        while right<len(s):
            while right < len(s) and s[right] == s[left]:
                right += 1

            count = right - left
            result.append(str(count))
            result.append(s[left])

            left = right

        return "".join(result)

"""
cns4 -> cns3 -> cns2 -> cns1
                cns2 <-                 
"""