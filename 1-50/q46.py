#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: YuLi
# @Time :2/1/2019 下午4:16
'''
给定一个没有重复数字的序列，返回其所有可能的全排列。
示例:
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''
class Solution:
    def permute(self, nums):
        def backtrack(res, nums, remain, n):
            if len(nums) == n:
                res.append(nums.copy())
                return
            for i in range(len(remain)):
                m = remain.pop(i)
                nums.append(m)
                backtrack(res, nums, remain, n)
                nums.pop()
                remain.insert(i, m)
        res = []
        backtrack(res, [], nums, len(nums))
        return res