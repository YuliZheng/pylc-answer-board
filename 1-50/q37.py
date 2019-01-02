#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: YuLi
# @Time :2/1/2019 下午3:51
'''
编写一个程序，通过已填充的空格来解决数独问题。
一个数独的解法需遵循如下规则：
数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。
Note:
给定的数独序列只包含数字 1-9 和字符 '.' 。
你可以假设给定的数独只有唯一解。
给定数独永远是 9x9 形式的。
'''

class Solution:
    def solveSudoku(self, board):

        strs = set(map(str, range(1, 10)))
        puzzles, row, col, area = [], [strs.copy() for _ in range(9)], [strs.copy() for _ in range(9)], [strs.copy() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.': puzzles.append((i, j))
                else: row[i].remove(board[i][j]); col[j].remove(board[i][j]); area[i//3*3+j//3].remove(board[i][j])

        def backTrack(puzzles, k, row, col, area, board):
            if k == len(puzzles): return True
            i, j = puzzles[k]
            sols = row[i] & col[j] & area[i//3*3+j//3]
            if len(sols) == 0: return False
            temp = board[i][j]
            for sol in sols:
                row[i].remove(sol); col[j].remove(sol); area[i//3*3+j//3].remove(sol); board[i][j] = sol
                if backTrack(puzzles, k + 1, row, col, area, board): return True
                row[i].add(sol); col[j].add(sol); area[i//3*3+j//3].add(sol); board[i][j] = temp
            return False

        backTrack(puzzles, 0, row, col, area, board)
'''回溯'''