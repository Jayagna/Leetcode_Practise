class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        l, r = 0 , len(s) - 1
        for l in range((len(s))//2):
            stored_l = s[l]
            s[l] = s[r]
            s[r] = stored_l
            r -= 1
        return s
        