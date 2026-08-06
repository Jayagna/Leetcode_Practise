class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        cbo,o,c =0,0,0

        for i in range(len(s)):
            if s[i] == '(':
                o += 1
            else:
                if o == c:
                    cbo += 1
                else:
                    c += 1

        return abs(o-c) + cbo