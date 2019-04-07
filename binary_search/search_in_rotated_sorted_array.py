"""Search in Rotated Sorted Array
https://www.lintcode.com/problem/search-in-rotated-sorted-array/description
"""

class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here
        left = 0
        right = len(A) - 1
        while left <= right:
            mid = left + (right-left) // 2
            if A[mid] == target:
                return mid
            # the left side is in order
            if A[mid] >= A[left]:
                if target >= A[left] and target < A[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # right sorted
            else:
                if target > A[mid] and target <= A[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

