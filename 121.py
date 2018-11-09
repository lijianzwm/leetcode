#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/11/9 18:09
# @Author  : lijian
# @Desc    : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        prices.reverse()

        ret = 0

        max_val =[prices[i] if i == 0 else 0 for i in range(len(prices))]

        for i in range(1, len(prices)):
            delta = max_val[i-1] - prices[i]
            ret = delta if delta > ret else ret
            max_val[i] = max(max_val[i-1], prices[i])

        print(max_val)

        return ret


if __name__ == "__main__":
    print(Solution().maxProfit([7,1,5,3,6,4]))