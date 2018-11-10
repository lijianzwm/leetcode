#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/11/10 11:49
# @Author  : lijian
# @Desc    : https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        import math
        for i in range(len(numbers)-1):
            if numbers[i] > target:
                 break
            delta = target - numbers[i]

            beg = i+1
            end = len(numbers)
            mid = int(math.floor((beg + end) / 2))

            while beg < end:
                if numbers[mid] < delta:
                    beg = mid + 1
                elif numbers[mid] > delta:
                    end = mid - 1
                else:
                    return [i+1, mid+1]
                mid = int(math.floor((beg+end)/2))


if __name__ == "__main__":
    Solution().twoSum([2,7,11,15], 9)


