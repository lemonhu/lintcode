"""Find Minimum in Rotated Sorted Array
https://www.lintcode.com/problem/find-minimum-in-rotated-sorted-array/description
"""

class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        left = 0
        right = len(nums) - 1
        res = 0
        target = nums[right]
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                right = mid - 1
                res = mid
            else:
                left += 1
        return nums[res]

