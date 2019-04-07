"""Find Peak Element
https://www.lintcode.com/problem/find-peak-element/description
"""

class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        left = 0
        right = len(A) - 1
        while left <= right:
            mid = left + (right-left) // 2
            if A[mid] > A[mid-1] and A[mid] > A[mid+1]:
                return mid
            elif A[mid] > A[mid+1]:
                right = mid - 1
            else:
                left = mid + 1
        return -1

