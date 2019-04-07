"""Reverse Linked List
https://www.lintcode.com/problem/reverse-linked-list/description
"""

"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        # write your code here
        dummy = None
        while head:
            dummy, head.next, head = head, dummy, head.next
        return dummy

