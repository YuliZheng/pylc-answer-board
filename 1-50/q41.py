#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: YuLi
# @Time :2/1/2019 下午4:01
'''
给定一个未排序的整数数组，找出其中没有出现的最小的正整数。
示例 1:
输入: [1,2,0]
输出: 3
示例 2:
输入: [3,4,-1,1]
输出: 2
示例 3:
输入: [7,8,9,11,12]
输出: 1
说明:
你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。
'''
'''直接在原空间上面的赋值
'''


class Solution:
    def firstMissingPositive(self, nums):

        l = len(nums)
        i = 0
        while i < l:
            num = nums[i]
            if num > 0:
                if num > l:
                    nums[i] = 0
                    i += 1
                else:
                    if not i == num - 1:
                        if not nums[num - 1] == num:
                            nums[num - 1], nums[i] = nums[i], nums[num - 1]
                        else:
                            nums[i] = 0
                            i += 1
                    else:
                        i += 1
            else:
                i += 1
        d_min = 0
        for j in range(l):
            if nums[j] <= 0:
                d_min = j + 1
                break
        if d_min == 0:
            d_min = l + 1
        return d_min
