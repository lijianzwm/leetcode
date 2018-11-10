#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/11/10 11:08
# @Author  : lijian
# @Desc    : https://leetcode.com/problems/min-stack/

class MinStack(object):
    """
    空间换时间，实现getMin
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.elements = []
        self.min = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.elements.append(x)
        cur_min = self.getMin()
        if cur_min is None or x < cur_min:
            self.min.append(x)
        else:
            self.min.append(cur_min)

    def pop(self):
        """
        :rtype: void
        """
        if len(self.elements) < 1:
            return None

        self.min.pop(len(self.min)-1)
        self.elements.pop(len(self.elements)-1)

    def top(self):
        """
        :rtype: int
        """
        if len(self.elements) < 1:
            return None
        return self.elements[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.min) < 1:
            return None
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == "__main__":
    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    print(s.getMin())
    print(s.pop())
    print(s.top())
    print(s.getMin())

