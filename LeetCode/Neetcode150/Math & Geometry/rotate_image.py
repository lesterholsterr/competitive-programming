# Initial - trivial when you can make a copy
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        copy = []
        for row in matrix:
            copy.append(row.copy())
        for i in range(n):
            row = copy[i]
            x = n-i-1
            for j in range(n):
                matrix[j][x] = row[j]

# Neetcode - in place solution
# A 90 degree rotation is like a quadruple swap - a, b, c, d = b, c, d, a
# Hard part is finding the relation between each (a, b, c, d) and grouping them up
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix)-1
        while l < r:
            for i in range(r-l):
                top, bottom = l, r # because matrix is square
                topLeft = matrix[top][l+i]
                matrix[top][l+i] = matrix[bottom-i][l]
                matrix[bottom-i][l] = matrix[bottom][r-i]
                matrix[bottom][r-i] = matrix[top+i][r]
                matrix[top+i][r] = topLeft
            l += 1
            r -= 1
