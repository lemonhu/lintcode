"""Longest Consecutive Sequence
https://www.lintcode.com/problem/longest-consecutive-sequence/description
"""

class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, num):
        # write your code here
        num.sort()
        res = 1
        cnt = 1
        for i in range(1, len(num)):
            if num[i] == num[i-1]:
                continue
            elif num[i] == num[i-1] + 1:
                cnt += 1
                res = max(res, cnt)
            else:
                cnt = 1
        return res

