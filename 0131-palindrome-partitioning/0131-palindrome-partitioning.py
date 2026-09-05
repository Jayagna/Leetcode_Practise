class Solution:
    def partition(self, s: str) -> List[List[str]]:
        final = []

        def dfs(part,i):
            if i == len(s): 
                final.append(part.copy())
                return

            for j in range(i,len(s)):
                left = s[i:j+1]
                if left == left[::-1]:
                    part.append(left)
                    dfs(part,j+1)
                    part.pop()

        dfs([],0)
        return final