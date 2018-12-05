#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: YuLi
# @Time :5/12/2018 下午7:45
'''罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
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
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。
示例 1:
输入: "III"
输出: 3
示例 2:
输入: "IV"
输出: 4
示例 3:
输入: "IX"
输出: 9
示例 4:
输入: "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.
示例 5:
输入: "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.
'''

'''
我的做法
'''
class Solution:
    def romanToInt(self, s):
        ii,vv,xx,ll,cc,dd,mm=0,0,0,0,0,0,0
        for i in range(len(s)):
            if(s[i]=='M'):
                mm+=1
            elif(s[i]=='D'):
                dd+=1
            elif(s[i]=='C'):
                if i+1<len(s)and(s[i+1]=='D' or s[i+1]=='M'):
                    cc-=1
                else:
                    cc+=1
            elif(s[i]=='L'):
                ll+=1
            elif(s[i]=='X'):
                if i+1<len(s)and(s[i+1]=='L' or s[i+1]=='C'):
                    xx-=1
                else:
                    xx+=1
            elif(s[i]=='V'):
                vv+=1
            elif(s[i]=='I'):
                if i+1<len(s)and(s[i+1]=='V' or s[i+1]=='X'):
                    ii-=1
                else:
                    ii+=1
        return ii*1+vv*5+xx*10+ll*50+cc*100+dd*500+mm*1000

'''
直接对字母计数
除了那些放在特定前面的
'''

class Solution:
    def romanToInt(self, s):
        convert = {"I":1,"IV":4,"V":5,"IX":9,"X":10,"XL":40,"L":50,"XC":90,"C":100,"CD":400,"D":500,"CM":900,"M":1000}
        len_n = len(s)
        n = 0
        i = 0
        while(i < len_n):
            key = s[i:i+2]
            if key in convert:
                n+=convert[key]
                i+=2
                continue
            key = s[i]
            if key in convert:
                n+=convert[key]
                i+=1
        return n