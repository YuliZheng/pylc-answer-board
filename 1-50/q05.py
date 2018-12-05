#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: YuLi
# @Time :5/12/2018 下午8:27
'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：
输入: "cbbd"
输出: "bb"
'''

class Solution:
    def longestPalindrome(self, s):
        n=len(s)
        if n==0:
            return ""
        t=0
        mid=0
        max1=0
        max2=0
        for i in range(n):
            l,r=i,i
            while(l>=0 and r<n and s[l]==s[r]):
                l,r=l-1,r+1
            max1=r-l-1
            if(i!=n-1):
                l,r=i,i+1
                while(l>=0 and r<n and s[l]==s[r]):
                    l,r=l-1,r+1
                max2=r-l-1
            else:max2=0
            if max(max1,max2)>t:
                t=max(max1,max2)
                mid=i
        return s[mid-(t-1)//2:mid+(t+2)//2]
'''
就是对每个扩充
'''

'''
标答
'''

class Solution:
    def longestPalindrome(self, s):
        if len(s) < 2 or s == s[::-1]:
            return s
        max_len = 1
        start = 0
        for i in range(1, len(s)):
            even = s[i - max_len: i + 1]
            odd = s[i - max_len - 1: i + 1]
            if i - max_len - 1 >= 0 and odd == odd[::-1]:
                start = i - max_len - 1
                max_len += 2
                continue
            if i - max_len >= 0 and even == even[::-1]:
                start = i - max_len
                max_len += 1
        return s[start: start + max_len]
'''
每次不直接扩充
末尾元素作指示
'''
