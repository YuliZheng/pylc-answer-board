#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: YuLi
# @Time :5/12/2018 下午8:57
'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
'''

class Solution:
    n = 0

    def lengthOfLongestSubstring(self, s):
        r = 0
        i = 0
        while i < len(s):
            m = self.expand(i, s)
            r = m if m > r else r
            i = self.n
        return r
    def expand(self, i, s):
        count = i + 1
        dic = {}
        dic[s[i]] = i
        while count < len(s):
            if (s[count] in dic):
                self.n = dic[s[count]] + 1
                break
            else:
                dic[s[count]] = count
                count = count + 1

        if count == len(s):
            self.n = count
        return count - i

'''
对每个字符找到他后面的最长
'''

class Solution:
    def lengthOfLongestSubstring(self, s):
        l=0
        start=0
        dict={}
        for i in range(len(s)):
            cur=s[i]
            if cur not in dict:
                dict[cur]=i
            else:
                if dict[cur]+1>start:
                    start=dict[cur]+1
                dict[cur]=i
            if i-start+1>l:
                l=i-start+1
        return l

'''
把还未重复的记录
如果重复了就从相同字母下一个开始    
'''