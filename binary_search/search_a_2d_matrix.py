"""Search a 2D Matrix
https://www.lintcode.com/problem/search-a-2d-matrix/description
"""

class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if matrix == []:
            return False
        m = len(matrix) - 1
        n = len(matrix[0]) - 1
        i, j = m, 0
        while i >= 0 and j <= n:
            if matrix[i][j] < target:
                j += 1
            elif matrix[i][j] > target:
                i -= 1
            else:
                return True
        return False

