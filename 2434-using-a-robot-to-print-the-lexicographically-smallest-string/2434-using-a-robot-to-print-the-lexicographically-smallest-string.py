class Solution:
    def robotWithString(self, s: str) -> str:
        minsuff = ['{']*(len(s)+1)

        for i in range(len(s)-1,-1,-1):
            minsuff[i] = min(minsuff[i+1],s[i])

        t,p = [],[]

        for i in range(len(s)):
            t.append(s[i])

            while t and t[-1] <= minsuff[i+1]:
                p.append(t.pop())

        return "".join(p)