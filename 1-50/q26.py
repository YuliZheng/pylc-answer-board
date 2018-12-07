#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: YuLi
# @Time :7/12/2018 下午9:56
'''
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
示例 1:
给定数组 nums = [1,1,2],

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。

你不需要考虑数组中超出新长度后面的元素。
示例 2:
给定 nums = [0,0,1,1,1,2,2,3,3,4],

函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

你不需要考虑数组中超出新长度后面的元素。
'''

class Solution:
    def removeDuplicates(self, nums):
        index=0
        length=len(nums)
        while(index<length):
            if index>0 and nums[index]==nums[index-1]:
                nums.pop(index)
                length-=1
            else:
                index+=1
        return index

'''
一次遍历
'''
'''
别人有的直接集合
'''