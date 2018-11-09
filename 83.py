#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/11/9 13:12
# @Author  : lijian
# @Desc    : https://leetcode.com/problems/remove-duplicates-from-sorted-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        注意处理None
        """
        if head is None:
            return head

        cur = head
        unique = head
        while cur:
            if unique.val != cur.val:
                unique.next = cur
                unique = cur
            cur = cur.next

        unique.next = None
        return head

if __name__ == "__main__":
    pass