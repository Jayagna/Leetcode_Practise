class Solution:
    def maxDepth(self, s: str) -> int:
        op,cl = 0,0
        res = 0

        for i in s:
            if i == '(':
                op += 1
            if i == ')':
                cl += 1
            res = max(res,(op-cl))

        return res