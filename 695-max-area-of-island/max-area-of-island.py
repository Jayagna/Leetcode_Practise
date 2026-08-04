class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        res = 0

        def dfs(r,c):
            stack = []
            stack.append((r,c))
            tot = 1
            grid[r][c] = 0

            while stack:
                row,col = stack.pop()
                for dr,dc in dirs:
                    nr = dr + row
                    nc = dc + col

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        tot += 1
                        stack.append((nr,nc))

            nonlocal res
            res = max(res,tot)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    dfs(i,j)

        return res