#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/11/9 15:24
# @Author  : lijian
# @Desc    : https://leetcode.com/problems/maximum-depth-of-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        树的最大深度，DFS即可
        """
        def dfs(root):
            if root is None:
                return 0

            return 1+max(dfs(root.left), dfs(root.right))

        return dfs(root)