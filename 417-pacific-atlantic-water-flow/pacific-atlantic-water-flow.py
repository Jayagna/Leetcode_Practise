class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        result = []

        pacific = set()
        atlantic = set()

        def dfs(r,c,v_set,curr_height):
            if r<0 or c<0 or r>=rows or c>=cols or heights[r][c] < curr_height or (r,c) in v_set:
                return
            v_set.add((r,c))

            dfs(r-1,c,v_set,heights[r][c])
            dfs(r+1,c,v_set,heights[r][c])
            dfs(r,c-1,v_set,heights[r][c])
            dfs(r,c+1,v_set,heights[r][c])

        for r in range(rows):
            dfs(r,0,pacific,heights[r][0])
            dfs(r,cols-1,atlantic,heights[r][cols-1])

        for c in range(cols):
            dfs(0,c,pacific,heights[0][c])
            dfs(rows-1,c,atlantic,heights[rows-1][c])

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])

        return result