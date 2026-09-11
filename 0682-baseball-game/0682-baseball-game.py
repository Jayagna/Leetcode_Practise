class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for val in operations:
            if val == "+":
                x = stack[-1]
                y = stack[-2]
                stack.append(x+y)
            elif val == "C":
                stack.pop()
            elif val == "D":
                x = stack[-1]
                stack.append(2*x)
            else:
                stack.append(int(val))

        return sum(stack)