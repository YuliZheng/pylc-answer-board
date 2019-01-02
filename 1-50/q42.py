#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: YuLi
# @Time :2/1/2019 下午4:05
'''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
示例:
输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
'''

'''
一根柱子如果比左边都高或者比右边都高才用
'''


class Solution:
    def trap(self, height):

        l = len(height)
        m = set()
        c_l = 0
        c_r = 0
        for i in range(l):
            if height[i] > c_l:
                m.add(i)
                c_l = height[i]
            if height[l - 1 - i] > c_r:
                m.add(l - 1 - i)
                c_r = height[l - 1 - i]
        m = sorted(list(m))
        r = 0
        for i in range(len(m) - 1):
            tall = min(height[m[i]], height[m[i + 1]])
            for j in height[m[i] + 1:m[i + 1]]:
                r += tall - j if j <= tall else 0
        return r