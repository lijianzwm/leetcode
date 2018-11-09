#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/11/9 17:34
# @Author  : lijian
# @Desc    : https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        递归，使用特殊值来标记是否是平衡二叉树
        """

        def depth(root):

            if root is None:
                return 0

            l_depth = depth(root.left)
            r_depth = depth(root.right)

            if l_depth is False or r_depth is False:
                return False

            if abs(l_depth - r_depth) > 1:
                return False

            return max(l_depth, r_depth)+1


        if depth(root) is not False:
            return True
        else:
            return False








