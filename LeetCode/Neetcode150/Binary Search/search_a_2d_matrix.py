class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        # Overall: Did this one cause friend sent it to me. Didn't realize it was part of Neetcode.
        # Leaps (for the better solution)
        # - The given matrix can be unrolled into a sorted 1-dimensional array
        # - How do you find out which ROW and COLUMN the "mid" point is on?

        # Initial Solution
        m = len(matrix)
        n = len(matrix[0])
        row = []

        l, r = 0, m - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][n-1] >= target:
                row = matrix[mid]
                break
            else:
                l = mid + 1

        if len(row) == 0:
            return False

        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False

        # Better Solution
        n, m = len(matrix), len(matrix[0])
        left, right = 0, n * m - 1

        while left <= right:
            mid = (left + right) // 2
            num = matrix[mid // m][mid % m]

            if num == target:
                return True

            if num < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
