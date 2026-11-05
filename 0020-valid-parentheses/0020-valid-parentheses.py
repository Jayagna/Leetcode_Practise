class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in "[{(":
                stack.append(char)
            elif char == "}" :
                if not stack or stack[-1] != "{":
                    return False
                else:
                    stack.pop()
            elif char == ")":
                if not stack or stack[-1] != "(":
                    return False
                else:
                    stack.pop()
            elif char == "]":
                if not stack or stack[-1] != "[":
                    return False
                else:
                    stack.pop()
        if len(stack):
            return False
        return True