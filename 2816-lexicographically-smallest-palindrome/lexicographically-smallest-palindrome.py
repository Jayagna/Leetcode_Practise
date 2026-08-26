class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        res = list(s)
        for i in range(len(res)//2):
            if res[i] != res[len(res)-i-1]:
                if ord(res[i]) > ord(res[len(res)-i-1]):
                    res[i] = res[len(res)-i-1]
                else:
                    res[len(res)-i-1] = res[i]

        return "".join(res)