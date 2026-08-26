class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        ans = 2

        for i in range(n-1):
            slopes = defaultdict(int)
            for j in range(i+1,n):
                dy = points[j][1] - points[i][1]
                dx = points[j][0] - points[i][0]

                if dx == 0:
                    m = float("inf")
                else:
                    m = dy/dx

                slopes[m] += 1

            if slopes:
                ans = max(ans, max(slopes.values()) + 1)

        return ans