#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: YuLi
# @Time :2/1/2019 下午3:33
'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
你可以假设数组中不存在重复的元素。
你的算法时间复杂度必须是 O(log n) 级别。
示例 1:
输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:
输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1
'''
'''
就是递归一下用，中间那个大于左边的话说明左边有序，不然就右边有序，然后接着递归
'''

class Solution:
    def search(self, nums, target):
        def binary(alist, data):
            n = len(alist)
            first = 0
            last = n - 1
            while first <= last:
                mid = (last + first) // 2
                if alist[mid] > data:
                    last = mid - 1
                elif alist[mid] < data:
                    first = mid + 1
                else:
                    return mid
            return -1
        left=0
        right=len(nums)-1
        res=-1
        while left<=right:
            mid = (left + right) //2
            if nums[mid] == target:
                return mid
            if nums[mid]<=nums[right]:
                #右边有序
                res = binary(nums[mid:right+1],target)
                if res==-1:
                    pass
                else:
                    return res+mid
                right = mid-1
            else:
                res = binary(nums[left:mid+1],target)
                if res==-1:
                    pass
                else:
                    return res+left
                left = mid+1
        return -1
