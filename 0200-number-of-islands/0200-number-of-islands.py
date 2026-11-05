class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        stack = []
        rows,cols = len(grid),len(grid[0])
        islands = 0
        dirs = [[-1,0],[0,1],[1,0],[0,-1]]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    grid[r][c] = "0"
                    stack.append((r,c))
                    while stack:
                        row,col = stack.pop()
                        for dr,dc in dirs:
                            nr = row + dr
                            nc = dc + col
                            if 0 <= nr < rows and  0 <= nc < cols and grid[nr][nc] == '1':
                                stack.append((nr,nc))
                                grid[nr][nc] = '0'

        return islands