#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/11/9 13:58
# @Author  : lijian
# @Desc    : https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        if p is None and q is not None:
            return False
        if q is None and p is not None:
            return False
        if p is None and q is None:
            return True

        if p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True
        else:
            return False


