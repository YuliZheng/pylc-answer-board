#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: YuLi
# @Time :2/1/2019 下午3:18
'''
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
必须原地修改，只允许使用额外常数空间。
以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''


class Solution:
    def nextPermutation(self, nums):
        tailIndex = 1
        startIndex = 2
        nums_length = len(nums)
        while startIndex <= nums_length and nums[-startIndex] >= nums[-startIndex + 1]:
            startIndex += 1
        if startIndex - 1 == nums_length:
            nums.reverse()
            return
        start = nums[-startIndex]
        next_start = 0
        for i in range(tailIndex, startIndex):
            if nums[-i] > start:
                next_start = i
                break
        nums[-startIndex], nums[-next_start] = nums[-next_start], nums[-startIndex]
        nums[-startIndex + 1:] = nums[:-startIndex:-1]
'''
先从右边开始找，找到第一个顺序对
然后把他和后面的比她大的最小的一个交换，然后把后面的反过来
'''
