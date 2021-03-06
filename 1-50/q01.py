#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: YuLi
# @Time :5/12/2018 下午9:17
'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的 两个 整数。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
示例:
给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''

'''
我的做法
'''


class Solution:
    def twoSum(self, nums, target):
        dic = {}
        for i in range(len(nums)):
            if (nums[i] in dic):
                return dic[nums[i]], i
            else:
                dic[target - nums[i]] = i

        return 0

