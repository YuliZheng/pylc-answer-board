#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: YuLi
# @Time :5/12/2018 下午7:41
'''
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
示例 1:
输入: ["flower","flow","flight"]
输出: "fl"
示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:
所有输入只包含小写字母 a-z 。
'''


'''
我的做法
'''

class Solution:
    def longestCommonPrefix(self, strs):
        answer = ""

        if strs == []:
            return ""
        for index in range(len(strs[0])):
            isineverystring = True
            for everystring in strs:
                if index >= len(everystring) or everystring[index] != strs[0][index]:
                    isineverystring = False
                    break
            if isineverystring:
                answer += (strs[0][index])
            else:
                break
        return answer

'''
直接遍历
'''
'''
别人做法
'''

class Solution:
    def longestCommonPrefix(self, strs):
        t=""
        if not strs:
            return ""
        else:
            min_str = min(strs,key = len)
            for i,v in enumerate(min_str):
                for j in strs:
                    if j[i] != v :
                        return min_str[:i]
            return min_str

'''也差不多'''