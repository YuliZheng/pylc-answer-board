#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: YuLi
# @Time :5/12/2018 下午5:40
'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例:
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
'''

'''
我的答案
'''


class Solution:

    def letterCombinations(self, digits):
        dic = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'],
               7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}

        if digits == '':
            return []
        answer = ['']
        for i in digits:
            i = int(i)
            lenth = len(answer)
            for h in range(lenth):
                string = answer.pop(0)
                for alpha in dic[i]:
                    newone = string + alpha
                    answer.append(newone)
        return answer

'''
我用了队列来搞
就相当于树的层次遍历
'''

'''
看看别人怎么做
'''

class Solution:
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []
        nums_letters = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        acc = [e for e in nums_letters[digits[0]]]
        for digit in digits[1:]:
            acc = [w1 + w2 for w1 in acc for w2 in nums_letters[digit]]
        return acc #列表生成器
