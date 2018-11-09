#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/11/9 12:46
# @Author  : lijian
# @Desc    : https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int

        当前层数的总数 = 上一层的总数+上上层的总数 <==> 斐波那契数列

        """

        a = 1
        b = 2

        if n < 3:
            return n

        result = 0
        for i in range(2, n):
            result = a + b
            a = b
            b = result

        return result

