class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for br in s:
            if br not in "]})":
                stack.append(br)

            elif br == ']':
                if not stack or stack.pop() != '[':
                    return False

            elif br == '}':
                if not stack or stack.pop() != '{':
                    return False

            elif br == ')':
                if not stack or stack.pop() != '(':
                    return False

        return len(stack) == 0