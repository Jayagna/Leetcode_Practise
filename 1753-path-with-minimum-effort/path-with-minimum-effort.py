from heapq import heappush,heappop
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows,cols = len(heights),len(heights[0])
        heap = [(0,0,0)]
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]

        distance = [[float("inf")]*cols for i in range(rows)]
        distance[0][0] = heights[0][0]
        vis = {(0,0)}

        while heap:
            effort,r,c = heappop(heap)
            if effort > distance[r][c]:
                continue
            if r == rows - 1 and c == cols - 1:
                return effort

            for dr, dc in dirs:

                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols:

                    diff = abs(
                        heights[r][c] - heights[nr][nc]
                    )

                    new_effort = max(effort, diff)

                    if new_effort < distance[nr][nc]:

                        distance[nr][nc] = new_effort

                        heappush(
                            heap,
                            (new_effort, nr, nc)
                        )
        return distance[-1][-1]

