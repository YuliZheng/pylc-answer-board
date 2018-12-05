#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: YuLi
# @Time :5/12/2018 下午5:00
'''
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
例如，给出 n = 3，生成结果为：
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

'''
我第一个思路
用到了dynamic programming
对每个可能
罗列出所有的闭包数的可能
'''
class Solution:
    def __init__(self):
        self.memo={}
    def generateParenthesis(self, n):
        if n in self.memo:
            return self.memo[n]
        elif n == 1:
            self.memo[1] = ["()"]
            return ["()"]
        else:
            def part(n, memoOfNum):
                if n in memoOfNum:
                    return memoOfNum[n]
                elif n == 1:
                    memoOfNum[1] = [[1]]
                    return [[1]]
                else:
                    possible = [[n]]
                    for first in range(1, n):
                        firstposs = part(first, memoOfNum)
                        lastposs = part(n - first, memoOfNum)
                        for i in firstposs:
                            for j in lastposs:
                                if not i + j in possible:
                                    possible.append(i + j)
                    memoOfNum[n] = possible
                    return memoOfNum[n]
                '''
                gives all the possible part of n
                '''

            memoNu = {}
            numpos = part(n, memoNu)
            numpos.pop(0)
            Parenthesis = self.generateParenthesis(n-1)
            p = len(Parenthesis)
            for index in range(p):
                Parenthesis[index] = '('+Parenthesis[index]+')'
            for possible in numpos:
                answer = [""]
                for numpart in possible:
                    partlist = self.generateParenthesis(numpart)
                    for index in range(len(answer)):
                        string = answer.pop(0)
                        for part in partlist:

                            answer.append(string + part)

                Parenthesis.extend(answer)
                answer = [""]
                self.memo[n] = Parenthesis
            Parenthesis = set(Parenthesis)
            Parenthesis = list(Parenthesis)
            return (Parenthesis)

'''
可以看到确实写得很长
效率也不高
'''


'''
别人的思路之一
'''

class Solution(object):
    def generateParenthesis(self, N):
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans

'''
这个确实是我没想到的
用了树的回溯算法
'''

'''
别人的思路之二
'''

class Solution(object):
    def generateParenthesis(self, N):
        if N == 0: return ['']
        ans = []
        for c in range(N):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(N-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans

'''
这个和我考虑的就很像
但他只算了第一个闭包
后面直接递归
而且没用动态规划
'''

'''
对上述方法的改进
'''

class Solution(object):
    def __init__(self):
        self.memo={}
    def generateParenthesis(self, N):
        if N==0:
            return ['']
        if N in self.memo:
            return self.memo[N]
        ans=[]
        for count in range(N):
            for first in self.generateParenthesis(count):
                for sencond in self.generateParenthesis(N-1-count):
                    ans.append("({}){}".format(first,sencond))
        self.memo[N]=ans
        return ans

'''
加上了动态规划
'''