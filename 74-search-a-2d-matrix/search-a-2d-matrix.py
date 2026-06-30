class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows = len(matrix)
        cols = len(matrix[0])

        top, bottom = 0, rows - 1

        # Binary search to find the possible row
        while top <= bottom:
            mid_row = top + (bottom - top) // 2

            if target < matrix[mid_row][0]:
                bottom = mid_row - 1

            elif target > matrix[mid_row][cols - 1]:
                top = mid_row + 1

            else:
                # Target must be somewhere in this row
                left, right = 0, cols - 1

                while left <= right:
                    mid_col = left + (right - left) // 2

                    if matrix[mid_row][mid_col] == target:
                        return True
                    elif matrix[mid_row][mid_col] < target:
                        left = mid_col + 1
                    else:
                        right = mid_col - 1

                return False

        return False
        