class MinStack(object):

    def __init__(self):
        self.s = []
        self.mini = []
        

    def push(self, val):
        self.s.append(val)
        if len(self.mini) == 0 or val <= self.mini[-1]:
            self.mini.append(val)

    def pop(self):
        res = self.s.pop()
        if len(self.mini)!= 0 and res == self.mini[-1]:
            self.mini.pop()

    def top(self):
        return self.s[-1]

    def getMin(self):
        if len(self.mini) != 0:
            return self.mini[-1]
        return 0  


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()