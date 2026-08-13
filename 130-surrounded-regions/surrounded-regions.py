class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows,cols = len(board),len(board[0])
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]
        vis = [[0]*cols for i in range(rows)]

        def dfs(r,c):
            vis[r][c] = 1
            for dr,dc in dirs:
                nr = r + dr
                nc = c + dc
                if 0<=nr<rows and 0<=nc<cols and board[nr][nc] == "O" and vis[nr][nc] == 0:
                    dfs(nr,nc)
            
        for r in range(rows):
            if board[r][0] == "O" and vis[r][0] == 0:
                dfs(r,0)
            if board[r][cols-1] == "O" and vis[r][cols-1] == 0:
                dfs(r,cols-1)
        for c in range(cols):
            if board[0][c] == "O" and vis[0][c] == 0:
                dfs(0,c)
            if board[rows-1][c] == "O" and vis[rows-1][c] == 0:
                dfs(rows-1,c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and vis[r][c] == 0:
                    board[r][c] = "X"

        return board