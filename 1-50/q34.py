#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: YuLi
# @Time :2/1/2019 下午3:38
'''
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
你的算法时间复杂度必须是 O(log n) 级别。
如果数组中不存在目标值，返回 [-1, -1]。
示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
'''

'''
就是一个变种的有序搜索
搜下界会就行
'''


class Solution:
    def searchRange(self, nums, target):

        def bmin(nums, target):
            if nums == []:
                return -1
            left = 0
            right = len(nums)
            while (left < right):
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            if left < len(nums) and nums[left] == target:
                return left
            return -1

        def bottom(nums, target):
            target_t = target + 1
            if nums == []:
                return -1
            left = 0
            right = len(nums)
            while (left < right):
                mid = (left + right) // 2
                if nums[mid] < target_t:
                    left = mid + 1
                else:
                    right = mid
            left -= 1
            if left < len(nums) and nums[left] == target:
                return left
            return -1

        return [bmin(nums, target), bottom(nums, target)]