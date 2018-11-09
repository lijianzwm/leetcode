#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/11/9 17:45
# @Author  : lijian
# @Desc    : https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        深搜找值
        """

        def dfs(root, cur_sum):
            if root is None:
                return False

            if root.right is None and root.left is None and cur_sum+root.val == sum:
                    return True

            return dfs(root.left, cur_sum+root.val) or dfs(root.right, cur_sum+root.val)

        return dfs(root, 0)


