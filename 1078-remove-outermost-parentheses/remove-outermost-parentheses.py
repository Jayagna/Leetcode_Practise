class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        opened,closed = 0,0
        res = []
        i,j = 0,0
        while j < len(s):
            if s[j] == ')':
                closed += 1
                j += 1
                
            elif s[j] == "(":
                opened += 1
                j += 1
                
            if opened == closed:
                res.append(s[i+1:j-1])
                i = j

        string = ''
        for s in res:
            string += s
        
        return string