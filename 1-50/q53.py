#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: YuLi
# @Time :2/1/2019 下午4:28
'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
示例:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:
如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
'''
class Solution:
    def maxSubArray(self, nums):
        t = 0
        a = nums[0]
        for n in nums:
            t += n
            if t > a:
                a = t
            if t < 0:
                t = 0

        return a