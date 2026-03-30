class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        
        for i in range(len(asteroids)):
            stack.append(asteroids[i])

            while len(stack) >= 2 and stack[-1]/(abs(stack[-1])) == -1 and stack[-2]/(abs(stack[-2])) == 1:
                if abs(stack[-1]) < abs(stack[-2]):
                    stack.pop()
                elif abs(stack[-1]) > abs(stack[-2]) :
                    x = stack.pop()
                    stack.pop()
                    stack.append(x)
                else:
                    stack.pop()
                    stack.pop()
        return stack
        