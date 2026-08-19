class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        dp = [[0]*len(grid[0]) for i in range(len(grid))]
        for i in range(len(grid[0])):
            if grid[0][i] == 1:
                break
            dp[0][i] = 1
        for i in range(len(grid)):
            if grid[i][0] == 1:
                break
            dp[i][0] = 1    

        for r in range(1,len(grid)):
            for c in range(1,len(grid[0])):
                if grid[r][c] == 0:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]

        return dp[len(grid)-1][len(grid[0])-1]