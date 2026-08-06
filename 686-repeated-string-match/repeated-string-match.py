class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        res = 1
        s = a
        while len(a) < len(b):
            res += 1
            a = a+s

        if b in a:
            return res
        if b in a+s:
            return res+1
        return -1