class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        max_len=1
        start=0
        def expand(left,right):
            nonlocal max_len,start
            while left>=0 and right<n:
                if s[left]==s[right]:
                    if max_len<right-left+1:
                        max_len=right-left+1
                        start=left
                    left,right=left-1,right+1
                else:
                    return
            return
        for i in range(n):
            expand(i,i)
            expand(i,i+1)
        return s[start:start+max_len]

