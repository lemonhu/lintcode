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
        m, n = len(matrix), len(matrix[0])
        start, end = 0, m * n - 1
        while start <= end:
            mid = start + (end - start) // 2
            x, y = mid // n, mid % n
            if matrix[x][y] < target:
                start = mid + 1
            elif matrix[x][y] > target:
                end = mid - 1
            else:
                return True
        return False

