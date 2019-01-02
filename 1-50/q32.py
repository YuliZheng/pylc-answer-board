#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: YuLi
# @Time :2/1/2019 下午3:32
'''
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
示例 1:
输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:
输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
'''


class Solution:
    def longestValidParentheses(self, s):

        stack = []

        a = 0
        r = len(s)
        for i in range(r):
            if stack == []:
                stack.append((s[i], i))
            else:
                top = stack[-1]
                if top[0] == '(' and s[i] == ')':
                    stack.pop()
                    top = stack[-1] if not stack == [] else (0, -1)
                    if i - top[1] > a:
                        a = i - top[1]
                else:
                    stack.append((s[i], i))
        return a