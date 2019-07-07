"""Longest Consecutive Sequence
https://www.lintcode.com/problem/longest-increasing-subsequence/description
"""

class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        length = len(nums)
        dp = [1] * length
        for i in range(length):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp) if dp else 0

