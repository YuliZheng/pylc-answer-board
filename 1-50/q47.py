#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: YuLi
# @Time :2/1/2019 下午4:17
'''
给定一个可包含重复数字的序列，返回所有不重复的全排列。
示例:
输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''
class Solution:
    def permuteUnique(self, nums):
        def backtrack(res, nums, remain, n):
            if len(nums) == n:
                k = ''
                for i  in nums:
                    k += str(i)
                if not k in res:
                    res.add(k)
                return
            for i in range(len(remain)):
                m = remain.pop(i)
                nums.append(m)
                backtrack(res, nums, remain, n)
                nums.pop()
                remain.insert(i, m)
        res = set()
        backtrack(res, [], nums, len(nums))
        a = []
        for i in res:
            k = []
            j = 0
            while j < len(i):
                if i[j] == '-':
                    k.append(int(i[j] + i[j+1]))
                    j += 2
                else:
                    k.append(int(i[j]))
                    j += 1
            a.append(k)
        return a