class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []
        for char in s:
            if char.isalnum():
                res.append(char)

        line = "".join(res).lower()

        return line == line[::-1]