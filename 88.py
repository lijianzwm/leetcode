#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/11/9 13:36
# @Author  : lijian
# @Desc    : https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        ret = nums1
        nums1 = list(nums1)
        ret.clear()
        cur1 = cur2 = 0
        print(nums1, nums2)
        for i in range(m+n):

            if cur1 < m and cur2 < n:
                if nums1[cur1] < nums2[cur2]:
                    ret.append(nums1[cur1])
                    cur1 += 1
                else:
                    ret.append(nums2[cur2])
                    cur2 += 1
                continue

            if cur1 >= m:
                ret.append(nums2[cur2])
                cur2 += 1
                continue

            if cur2 >= n:
                ret.append(nums1[cur1])
                cur1 += 1
                continue


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    Solution().merge(nums1, m, nums2, n)
    print(nums1)
