#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/11/10 11:35
# @Author  : lijian
# @Desc    : https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        s1 = []
        s2 = []

        cur = headA
        while cur:
            s1.append(cur)
            cur = cur.next

        cur = headB
        while cur:
            s2.append(cur)
            cur = cur.next

        s1.reverse()
        s2.reverse()

        intersection = None

        for i in range(min(len(s1), len(s2))):
            if s1[i] != s2[i]:
                break
            else:
                intersection = s1[i]
        return intersection






