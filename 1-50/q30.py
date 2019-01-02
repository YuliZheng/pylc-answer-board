#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: YuLi
# @Time :2/1/2019 下午3:14
'''
给定一个字符串 s 和一些长度相同的单词 words。在 s 中找出可以恰好串联 words 中所有单词的子串的起始位置。
注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。
示例 1:
输入:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出: [0,9]
解释: 从索引 0 和 9 开始的子串分别是 "barfoor" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
示例 2:
输入:
  s = "wordgoodstudentgoodword",
  words = ["word","student"]
输出: []
'''

'''
此题巨难
'''

import re


class Solution:
    def findSubstring(self, s, words):

        rows = len(words)
        word_count = {}
        for i in words:
            word_count[i] = words.count(i)
        if words == []:
            return []
        l = len(words[0])
        res = []
        valid = len(s) - rows * l + 1
        for i in range(valid):
            count = {}
            score = 0
            start = index = i
            while (index + l <= len(s) and s[index:index + l] in word_count):
                c = s[index:index + l]
                count[c] = count.get(c, 0) + 1
                if count[c] <= word_count[c]:
                    score += 1
                else:
                    break
                index += l
            if score == rows:
                res.append(start)

        return res
'''
抄的抄的
没啥好说的
'''