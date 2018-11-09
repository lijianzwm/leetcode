#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/11/9 18:02
# @Author  : lijian
# @Desc    : https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]

        last = [1, 1]

        for i in range(rowIndex-1):
            cur = [1]
            for j in range(len(last)-1):
                cur.append(last[j]+last[j+1])
            cur.append(1)
            last = cur

        return last






