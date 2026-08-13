class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        res = 0

        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j,0))

        while q:
            r,c,time = q.popleft()
            res = max(time,res)
            for dr,dc in dirs:
                nr = dr + r
                nc = dc + c

                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    q.append((nr,nc,time+1))
                
        for r in range(rows):
            for j in range(cols):
                if grid[r][j] == 1:
                    return -1

        return res