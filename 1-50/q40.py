#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: YuLi
# @Time :2/1/2019 下午3:58
'''
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。
说明：
所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。
示例 1:
输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例 2:
输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]
'''

class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        all_solution = []
        def backtrack(nums, remain, target):
            num = sum(nums)
            if num == target:
                if not nums in all_solution:
                    all_solution.append(nums.copy())
            elif num < target:
                if remain == []:
                    return
                else:
                    k = remain.pop()
                    backtrack(nums, remain, target)
                    nums.append(k)
                    backtrack(nums, remain, target)
                    nums.pop()
                    remain.append(k)
            else:
                return
        backtrack([], candidates, target)
        return all_solution