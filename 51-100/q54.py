#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: YuLi
# @Time :2/1/2019 下午4:28
'''
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
示例 1:
输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
示例 2:
输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]
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