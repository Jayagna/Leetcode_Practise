class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        @cache
        def dfs(r,c):
            if r == 0 and c == 0:
                if grid[0][0] == 1:
                    return 0
                return 1
            if r < 0 or c < 0:
                return 0
            if grid[r][c] == 1:
                return 0
            up = dfs(r-1,c)
            left = dfs(r,c-1)
            return up + left
        return dfs(rows-1,cols-1)