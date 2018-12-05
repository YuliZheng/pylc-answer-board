#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: YuLi
# @Time :5/12/2018 下午8:02
'''
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器，且 n 的值至少为 2。

图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

示例:
输入: [1,8,6,2,5,4,8,3,7]
输出: 49
'''

'''
这题我原本不会
'''

'''
答案
'''


class Solution:
    def maxArea(self, height):
        ran = len(height)
        maxV = 0
        i = 0
        j = ran - i - 1
        while (j - i > 0):
            if (height[i] > height[j]):
                if (height[j] * (j - i) > maxV):
                    maxV = height[j] * (j - i)
                j -= 1
            else:
                if (height[i] * (j - i) > maxV):
                    maxV = height[i] * (j - i)
                i += 1

        return maxV
'''
一开始头尾
重点是当一个比另一个矮的移动更高的没有好处
所以只能移动另一个
这样不断扫描可以在一次解决
'''