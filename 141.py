#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/11/9 18:46
# @Author  : lijian
# @Desc    : https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        快慢指针
        """
        if head is None:
            return False

        slow_ref = head
        fast_ref = head.next

        while slow_ref != fast_ref:
            if fast_ref is None:
                return False
            fast_ref = fast_ref.next
            if fast_ref == slow_ref:
                return True
            if fast_ref is None:
                return False
            fast_ref = fast_ref.next
            slow_ref = slow_ref.next

        return True




