"""Majority Element
https://www.lintcode.com/problem/majority-element/description
"""

class Solution:
    """
    @param: nums: a list of integers
    @return: find a  majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        res = nums[0]
        cnt = 0
        for num in nums:
            if res == num:
                cnt += 1
            else:
                if cnt == 0:
                    res = num
                else:
                    cnt -= 1
        return res

