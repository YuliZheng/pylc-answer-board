#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: YuLi
# @Time :2/1/2019 下午4:14
'''
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
你的目标是使用最少的跳跃次数到达数组的最后一个位置。
示例:
输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
说明:
假设你总是可以到达数组的最后一个位置。
'''
'''
这题答案给的是贪心
'''


class Solution:
    def jump(self, nums):

        n = len(nums)

        if n == 1:
            return 0

        start = 1

        end = nums[0]

        res = 1

        reached = False

        while end < n - 1:

            res += 1

            max_end = end

            for i in range(start, end + 1):

                if i + nums[i] > max_end:
                    max_end = i + nums[i]

                    reached = True

            if not reached:
                return -1

            reached = False

            start = end + 1

            end = max_end

        return res