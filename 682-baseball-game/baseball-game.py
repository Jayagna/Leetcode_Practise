class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        res = []
        for i in range(len(operations)):
            if operations[i] == '+':
                res.append(res[-1] + res[-2])
            elif operations[i] == 'C':
                res.pop()
            elif operations[i] == 'D':
                res.append(2*res[-1])
            else:
                res.append(int(operations[i]))
        sum = 0  
        for i in range(len(res)):
            sum += res[i]
        return sum
        