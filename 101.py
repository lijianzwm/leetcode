#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/11/9 14:05
# @Author  : lijian
# @Desc    : https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        镜像二叉树 <==> 左子树的镜像=右子树
        """

        def isMirror(r1, r2):
            if r1 is None and r2 is None:
                return True
            if r1 and r2 and r1.val == r2.val:
                return (isMirror(r1.left, r2.right) and isMirror(r1.right, r2.left))
            return False


        return isMirror(root, root)


if __name__ == "__main__":

    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

    root = TreeNode(1)
    print(Solution().isSymmetric(root))