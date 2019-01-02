#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: YuLi
# @Time :2/1/2019 下午3:11
'''
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
返回被除数 dividend 除以除数 divisor 得到的商。
示例 1:
输入: dividend = 10, divisor = 3
输出: 3
示例 2:
输入: dividend = 7, divisor = -3
输出: -2
说明:
被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。
'''

'''
这题考计算机中的表示
和算法关系不大
'''


class Solution:
    def divide(self, dividend, divisor):

        minussign = 1
        if dividend < 0:
            dividend = -dividend
            minussign = -minussign
        if divisor < 0:
            divisor = -divisor
            minussign = -minussign

        an = 0
        m, n = dividend, divisor
        while m >= n:
            t = n
            p = 1
            while m > t << 1:
                t <<= 1
                p <<= 1
            an += p
            m -= t
        an = an * minussign
        max_val = 2 ** 31
        return an if an < max_val else max_val - 1