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
        if nums[left] > nums[right]:
            while left + 1 < right:
                mid = left + (right-left) // 2
                if nums[mid] > nums[right]:
                    left = mid
                else:
                    right = mid
            return min(nums[left], nums[right])
        return nums[left]

