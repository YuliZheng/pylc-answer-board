#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: YuLi
# @Time :5/12/2018 下午8:16
'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
示例 1:
输入: 123
输出: 321
 示例 2:
输入: -123
输出: -321
示例 3:
输入: 120
输出: 21
'''

'''
首先做法
'''

class Solution:
    def reverse(self, x):
        y=0
        flag=0
        if x<0:
            flag=1
            x=-x
        while x!=0:
            bit=x%10
            y=y*10+bit
            x=x//10
        if y>>31 !=0:
            return 0
        if flag==1:
            y=-y
        if not isinstance(y,int):
            return 0
        return y

'''
用了位运算来判断
'''

'''
别人
'''

class Solution:
    def reverse(self, x):
        if x < 0:
            s = str(-x)
            y = s[::-1]
            z = -int(y)
        else:
            s = str(x)
            y = s[::-1]
            z = int(y)
        if -2**31<z<2**31-1:
            return z
        return 0

'''
::-1真的好用
'''