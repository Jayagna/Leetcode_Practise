class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        q = deque()
        island = 0
        rows,cols = len(grid),len(grid[0])
        dirs = [(-1,0),(0,1),(1,0),(0,-1)]

        def dfs(r,c):
            grid[r][c] = "0"
            for dr,dc in dirs:
                nr = r + dr
                nc = c + dc
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == "1":
                    grid[nr][nc] = "0"
                    dfs(nr,nc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    island += 1
                    dfs(r,c)

        return island