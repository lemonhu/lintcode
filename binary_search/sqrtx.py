"""Sqrt(x)
https://www.lintcode.com/problem/sqrtx/description
"""

class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        left = 0
        right = x
        res = 0
        while left <= right:
            mid = left + (right-left) // 2
            if mid * mid <= x:
                left = mid + 1
                res = mid
            else:
                right = mid - 1
        return res

