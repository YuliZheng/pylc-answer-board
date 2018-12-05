#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: YuLi
# @Time :5/12/2018 下午8:08
'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
示例 1:
输入: 121
输出: true
示例 2:
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:
输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
进阶:
你能不将整数转为字符串来解决这个问题吗？
'''

'''
我的思路
'''

class Solution:
    def isPalindrome(self, x):
        if x<0:
            return False
        i=1
        while(10**i<=x):
            i+=1
        for j in range(i//2):
            tail=(x//(10**j))%10
            head=(x//(10**(i-1-j)))%10
            if tail!=head:
                return False
        return True
'''
用mod取得末尾数字
//取得头数字
'''

'''
别人
'''


class Solution:
    def isPalindrome(self, x):

        if x >= 0 and str(x) == str(x)[::-1]:
            a = True
        else:
            a = False
        return a
'''
他们明明没按提示还比我快
'''