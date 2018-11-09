#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/11/9 15:28
# @Author  : lijian
# @Desc    : https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root is None:
            return []

        ret = []
        q = []

        q.append([root, 0])
        ret.append([root.val])

        while len(q):
            print(ret)
            cur, lv = q.pop(0)
            cur_v = []

            if cur.left is not None:
                q.append([cur.left, lv+1])
                cur_v.append(cur.left.val)

            if cur.right is not None:
                q.append([cur.right, lv+1])
                cur_v.append(cur.right.val)

            if len(cur_v) > 0:
                if len(ret) < lv+1+1:
                    ret.append([])
                ret[lv+1].extend(cur_v)

        ret.reverse()
        return ret

if __name__ == "__main__":

    class TreeNode:
        def __init__(self, x, left=None, right=None):
            self.val = x
            self.left = None
            self.right = None


    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))

    print(Solution().levelOrderBottom(root))


