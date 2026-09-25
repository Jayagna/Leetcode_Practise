class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = ''

        for i in range(len(strs[0])):
            for s in strs:
                if len(s) < i + 1 or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]

        return res