#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/11/10 12:15
# @Author  : lijian
# @Desc    : https://leetcode.com/problems/excel-sheet-column-title/

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        n -= 1
        if n < 26:
            return chr(65+n)
        return self.convertToTitle(n//26) + chr(65+ n % 26)
