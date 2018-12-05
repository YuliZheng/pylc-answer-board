#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: YuLi
# @Time :5/12/2018 下午7:48
'''
罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。
字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。
通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。
示例 1:
输入: 3
输出: "III"
示例 2:
输入: 4
输出: "IV"
示例 3:
输入: 9
输出: "IX"
示例 4:
输入: 58
输出: "LVIII"
解释: L = 50, V = 5, III = 3.
示例 5:
输入: 1994
输出: "MCMXCIV"
解释: M = 1000, CM = 900, XC = 90, IV = 4.
'''


'''
第一思路
'''

class Solution:
    def intToRoman(self, num):
        ii=num%5
        vv=1 if num%10>=5 else 0
        xx=num%50//10
        ll=1 if num%100>=50 else 0
        cc=num%500//100
        dd=1 if num%1000>=500 else 0
        mm=num%5000//1000
        answer=""
        answer+=('M'*mm)
        if cc==4:
            answer+="CD" if dd==0 else "CM"
        else:
            answer+=("D"*dd)
            answer+=("C"*cc)
        if xx==4:
            answer+="XL" if ll==0 else"XC"
        else:
            answer+=("L"*ll)
            answer+=("X"*xx)
        if ii==4:
            answer+="IV" if vv==0 else"IX"
        else:
            answer+=("V"*vv)
            answer+=("I"*ii)
        return answer

'''
直接
'''

'''
别人
'''

class Solution:
    def intToRoman(self, num):
        res = ''
        token = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        for n, t in token:
            while num >= n:
                res += t;
                num -= n
        return res

'''
相当于直接元件去凑
'''