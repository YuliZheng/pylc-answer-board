#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: YuLi
# @Time :5/12/2018 下午5:18
'''
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
注意：
答案中不可以包含重复的四元组。
示例：
给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''


'''
我的思路
'''


class Solution:
    def fourSum(self, nums, target):
        s_nums = set(nums)
        p_nums = []
        for num in s_nums:
            num_count = nums.count(num)
            if num_count >= 4:
                p_nums.extend([num] * 4)
            else:
                p_nums.extend([num] * num_count)
        p_nums.sort()

        def twoSum(nums, target):
            dic = {}
            answer = []
            for i in range(len(nums)):
                if (nums[i] in dic):
                    answer.append([dic[nums[i]], nums[i]])
                else:
                    dic[target - nums[i]] = nums[i]

            return answer

        reply = []
        l = len(p_nums)

        for FirstIndex in range(l - 3):
            for SecondIndex in range(FirstIndex + 1, l - 2):
                Targetnow = target - p_nums[FirstIndex] - p_nums[SecondIndex]
                for Sumtwo in twoSum(p_nums[SecondIndex + 1:], Targetnow):
                    if not Sumtwo == 0:
                        Sumtwo.sort()
                        c = [p_nums[FirstIndex], p_nums[SecondIndex]]
                        c.extend(Sumtwo)
                        if not c in reply:
                            reply.append(c)
        return reply


'''
对每个二元组
从剩下的里面用二数找到和相同的
时间复杂度应该是
2+1=3
但是常数比较大
排名好像很靠后
'''

'''
看一下别人的做法
'''


class Solution:
    def fourSum(self, nums, target):
        """
        method1 112ms 97.93%
        先做排序，选定前两个数后，双指针指向后两个数的可选范围的边界，根据sum与target的关系，移动指针
        trick1: 前两个数在遍历过程中，遇到连续的相同数时跳过
        trick2: 前两个数固定后，将后两个数可选范围内的极值同target比较，极端情况下可以提前终止该轮或者整个循环
        trick3: 每次均求和同target比较计算次数太多，可以事先对target和已确定数做减法替代
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        res = []
        nums.sort()
        length = len(nums)

        for i, x in enumerate(nums[:-3]):
            target1 = target - x
            if sum(nums[i:i + 4]) > target:
                break #极端情况后面的数直接超过
            elif sum(nums[-3:]) < target1 or (i > 0 and x == nums[i - 1]):
                continue #太小或者连续n个一样
            for j in range(i + 1, length - 2):
                target2 = target1 - nums[j]
                if nums[j + 1] + nums[j + 2] > target2:
                    break
                elif nums[-2] + nums[-1] < target2 or (j > i + 1 and nums[j] == nums[j - 1]):
                    continue
                k, l = j + 1, length - 1
                while k < l:
                    temp = nums[k] + nums[l]
                    if temp > target2:
                        l -= 1
                    elif temp < target2:
                        k += 1
                    else:
                        res.append([x, nums[j], nums[k], nums[l]])
                        while k < l and nums[k] == nums[k + 1]:
                            k += 1
                        while k < l and nums[l] == nums[l - 1]:
                            l -= 1
                        k, l = k + 1, l - 1
        return res
'''
这个做法比我快了n倍
他改进了有序状态下两个数的查找
确实有序状态下如果
用双指针可能比字典更快
虽然都是常数
他还用了几个技巧
'''
# method2
#         def findNsum(nums,target,N,result,results):
#             # early termination
#             if len(nums) < N or N < 2 or target < nums[0] * N or target > nums[-1]*N:
#                 return

#             # two pointer solve sorted 2-sum problem
#             if N == 2:
#                 l,r = 0, len(nums) - 1
#                 while l < r:
#                     s = nums[l] + nums[r]
#                     if s == target:
#                         results.append(result + [nums[l], nums[r]])
#                         l += 1
#                         while l < r and nums[l] == nums[l-1]:
#                             l += 1
#                     elif s < target:
#                         l += 1
#                     else:
#                         r -= 1

#             # recursively reduce N
#             else:
#                 for i in range(len(nums) - N + 1):
#                     if i == 0 or (i > 0 and nums[i-1] != nums[i]):
#                         findNsum(nums[i+1:],target-nums[i],N-1,result+[nums[i]],results)

#         results = []
#         findNsum(sorted(nums),target,4,[],results)
#         return results
'''
上面是n数查找问题
就是递归成n-2然后用二数查找
'''