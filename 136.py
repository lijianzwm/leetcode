#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/11/9 18:43
# @Author  : lijian
# @Desc    : https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        base = 0
        for num in nums:
            base ^= num

        return base


if __name__ == "__main__":
    print(Solution().singleNumber([1,2,2,3,3]))


