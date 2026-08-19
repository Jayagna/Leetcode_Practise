class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        @cache
        def dfs(r,c):
            if r == 0 and c == 0:
                return grid[0][0]
            if r < 0 or c <0:
                return float("inf")

            up = grid[r][c] + dfs(r-1,c)
            left = grid[r][c] + dfs(r,c-1)
            return min(up,left)
        return dfs(rows-1,cols-1)