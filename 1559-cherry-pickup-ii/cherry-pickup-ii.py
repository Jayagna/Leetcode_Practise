class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        @cache
        def dfs(i,j1,j2):
            if j1 < 0 or j1 >= cols or j2<0 or j2 >= cols:
                return -float("inf")
            elif i == rows-1:
                if j1 == j2:
                    return grid[i][j1]
                return grid[i][j1] + grid[i][j2]

            maxi = 0
            for v in range(-1,2):
                for b in range(-1,2):
                    if j1 == j2:
                        maxi = max(maxi,grid[i][j1] + dfs(i+1,j1+v,j2+b))
                    else:
                        maxi = max(maxi, grid[i][j1] + grid[i][j2] + dfs(i+1,j1+v,j2+b))
            
            return maxi

        return dfs(0,0,cols-1)