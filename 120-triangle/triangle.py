class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[0] * len(row) for row in triangle]

        dp[0][0] = triangle[0][0]

        rows = len(triangle)

        for r in range(1, rows):
            # left edge
            dp[r][0] = triangle[r][0] + dp[r-1][0]

            # right edge
            dp[r][-1] = triangle[r][-1] + dp[r-1][-1]

        # middle elements
        for r in range(2, rows):
            for c in range(1, len(triangle[r]) - 1):
                dp[r][c] = triangle[r][c] + min(
                    dp[r-1][c],
                    dp[r-1][c-1]
                )

        return min(dp[-1])