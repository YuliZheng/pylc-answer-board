#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: YuLi
# @Time :2/1/2019 下午4:29
'''
class Solution:
    def spiralOrder(self, matrix):
        def huaquan(matrix,index):
            ans = []
            m = len(matrix)
            n = len(matrix[0])
            i, j = index, index
            if i == m - i - 1:
                for j in range(index, n-index):
                    ans.append(matrix[i][j])
                return ans
            elif j == n - j - 1:
                for i in range(index, m-index):
                    ans.append(matrix[i][j])
                return ans
            else:
                for j in range(index, n-index):
                    ans.append(matrix[i][j])
                for i in range(index+1, m-index):
                    ans.append(matrix[i][j])
                for j in range(n-index-2, index-1,-1):
                    ans.append(matrix[i][j])
                for i in range(m-index-2,index,-1):
                    ans.append(matrix[i][j])
                return ans
        if len(matrix) == 0:
            return []
        l = []
        r = min(len(matrix),len(matrix[0]))
        for index in range((r+1)//2):
            l.extend(huaquan(matrix, index))
        return l
'''
class Solution:
    def canJump(self, nums):
        if nums == []:
            return True
        l = len(nums)
        loc = 0
        while loc < l-1:
            start = loc
            jump = nums[start]
            value = 0
            m = 0
            if start + jump >= l-1:
                return True
            for i in range(1,jump+1):
                if nums[start+i] + i > value:
                    m = i
                    value = nums[start+i] + i
            loc = start + m
            while nums[loc] == 0 and loc > start:
                loc -= 1
            if loc == start:
                return False
        return True