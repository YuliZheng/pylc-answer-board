#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: YuLi
# @Time :5/12/2018 下午8:20
'''
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
请你实现这个将字符串进行指定行数变换的函数：
string convert(string s, int numRows);
示例 1:
输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
示例 2:
输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G
'''
'''这题挺有意思的'''

class Solution:
    def convert(self, s, numRows):
        number=2*numRows-2
        if number==0:
            return s
        count=0
        lenth=len(s)
        numPattern=lenth//number
        zs=['0']*lenth
        numOfRowsRemain=lenth%number
        RowsRemainBefore=[]
        n=numOfRowsRemain
        z=[]
        if(n>0):
            for i in range(number//2+1):
                if i==0:
                    RowsRemainBefore.append(0)
                else:
                    m=RowsRemainBefore[-1]
                    if i-1<n:
                        m+=1
                    if n-1>number-i:
                        m+=1
                    RowsRemainBefore.append(m)
        for Index in range(lenth):
            count=Index//number
            IndexInPattern=Index-count*number
            row=min(IndexInPattern,number-IndexInPattern)
            newIndex=RowsRemainBefore[row] if n!=0 else 0
            for i in range(row):
                newIndex+= numPattern if i==0 else numPattern*2
            if (IndexInPattern==0 or IndexInPattern==number//2):
                newIndex+=count
            else:
                newIndex+=2*count
                if(IndexInPattern>number//2):
                    newIndex+=1
            zs[newIndex]=s[Index]
            z.append(newIndex)
        return ''.join(zs)

'''
当时觉得这反正可逆映射
把他的指标的逆映射构造出来不就完了
'''

'''
看看
别人
'''

class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        L = [''] * numRows
        index, step = 0, 1
        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        return ''.join(L)
'''
好耍赖啊
把每一行看成字符串
然后直接添加
然后字符串直接组合
这个思维不错
'''