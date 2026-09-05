class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols = len(board),len(board[0])
        vis = set()
        dirs = [(-1,0),(0,1),(1,0),(0,-1)]

        def dfs(r,c,ind):
            vis.add((r,c))
            if ind == len(word):
                return True
            for dr,dc in dirs:
                nr = dr + r
                nc = dc + c
                if 0<=nr<rows and 0<=nc<cols and board[nr][nc] == word[ind] and (nr,nc) not in vis:
                    if dfs(nr,nc,ind+1):
                        return True
            vis.remove((r,c))
            return False

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r,c,1):
                        return True
        return False