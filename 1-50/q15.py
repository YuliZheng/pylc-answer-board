#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: YuLi
# @Time :5/12/2018 下午5:58

'''
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。
例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

'''
我的做法
'''
class Solution:
    def threeSum(self, nums):
        numsset=set(nums)
        numsuse=[]
        for num in numsset:
            freq=nums.count(num)
            if freq>=3:
                numsuse.extend([num]*3)
            else:
                numsuse.extend([num]*freq)
        nums=numsuse
        n=len(nums)
        dic={}
        answer=[]
        answersets=set()
        for index in range(n):
            purpnum=0-nums[index]
            dic[purpnum]=[nums[index],index]
        for indexF in range(n):
            for indexS in range(indexF+1,n):
                currnum=nums[indexF]+nums[indexS]
                if currnum in dic:
                    if dic[currnum][1]!=indexF and dic[currnum][1]!=indexS:
                        oneanswer=[nums[indexF],nums[indexS],dic[currnum][0]]
                        answersort=sorted(oneanswer)
                        answerstr=[str(i) for i in answersort]
                        answerhash=''.join(answerstr)
                        if not answerhash in answersets:
                            answer.append(oneanswer)
                            answersets.add(answerhash)
        return(answer)


'''
先用set化为没什么重复的
然后在对所有数建立需求索引
然后遍历二元组找到解
最后对解的重复处理
我原本想直接hash
可是列表不能hash
我就排序后转化为string
算是个技巧
'''

'''
我的速度比较慢
大概打败二十
看看别人怎么做
放一个比我快2倍的做法
'''

class Solution:
    def threeSum(self, nums):

        tem=dict()
        res=[]
        for i in nums:
            tem[i]=tem.get(i,0)+1
        left=list(filter(lambda x: x<0, tem))
        right=list(filter(lambda x :x>=0,tem))
        if 0 in right and tem[0] >2:
            res.append([0,0,0])
        for i in left:
            for j in right:
                mid=-i-j
                if mid in tem:
                    if mid in (i,j) and tem[mid]>1:
                        res.append([i,mid,j])
                    elif mid<i or mid>j:
                        res.append([i,mid,j])
        return res

'''
我觉得还是挺叼的
首先三个数不可能都正都负
一个数只用在正
一个数只用在负
这样就比我快挺多
然后处理重复由于三个数
他就直接按两个重复或者都是0来处理
'''