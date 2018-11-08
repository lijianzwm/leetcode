#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/11/8 19:20
# @Author  : lijian
# @Desc    : https://leetcode.com/problems/sqrtx/


class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        beg = 1
        end = x
        mid = int((beg+end)/2)

        while mid != beg:
            if mid*mid == x:
                return mid
            elif mid*mid > x:
                end = mid
            else:
                beg = mid
            mid = int((beg + end) / 2)

        return mid




s = Solution()
print(s.mySqrt(4))