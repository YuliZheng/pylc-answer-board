#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: YuLi
# @Time :5/12/2018 下午5:11
'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
示例 1:
输入: "()"
输出: true
示例 2:
输入: "()[]{}"
输出: true
示例 3:
输入: "(]"
输出: false
示例 4:
输入: "([)]"
输出: false
示例 5:
输入: "{[]}"
输出: true
'''

'''
我写的
'''


class Solution:
    def isValid(self, s):
        l = []
        d = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if not char in d:
                l.append(char)
            else:
                if l == [] or not l.pop() == d[char]:
                    return False
        return not l

'''
用了dict省时
'''