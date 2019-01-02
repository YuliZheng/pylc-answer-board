#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: YuLi
# @Time :2/1/2019 下午4:27
'''
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给定一个整数 n，返回 n 皇后不同的解决方案的数量。
示例:
输入: 4
输出: 2
解释: 4 皇后问题存在如下两个不同的解法。
[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
'''
class Solution:
    def totalNQueens(self, n):
        def recursive(mark, cur, ret):

            if cur == len(mark):
                ret[0] += 1
                return

            for i in range(len(mark)):
                mark[cur], down = i, True
                for j in range(cur):
                    if mark[j] == i or abs(i-mark[j]) == cur - j:
                        down = False
                        break
                if down:
                    recursive(mark, cur+1, ret)


        ret = [0]
        recursive([None]*n, 0, ret)
        return ret[0]