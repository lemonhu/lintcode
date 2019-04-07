"""First Position of Target
https://www.lintcode.com/problem/first-position-of-target/description
"""

class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binarySearch(self, nums, target):
        # write your code here
        left = 0
        right = len(nums) - 1
        index = -1
        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                index = mid
                break
        while index - 1 >= 0:
            if nums[index] == nums[index-1]:
                index -= 1
            else:
                break
        return index

