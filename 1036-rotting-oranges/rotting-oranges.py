class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]
        visited = set()

        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j,0))
                    visited.add((i,j))
        
        res = 0
        while q:
            row,col,time = q.popleft()
            res = time

            for dr,dc in dirs:
                nr = dr + row
                nc = dc + col

                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1 and (nr,nc) not in visited:
                    grid[nr][nc] = 2
                    q.append((nr,nc,time+1))
                    visited.add((nr,nc))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
                    
        return res