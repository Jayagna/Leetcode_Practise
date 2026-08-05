class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        rep = defaultdict()
        rev = defaultdict()

        for w,r in zip(s,t):
            if w in rep and rep[w] != r:
                return False
            if r in rev and rev[r] != w:
                return False
            rep[w] = r
            rev[r] = w

        return True 