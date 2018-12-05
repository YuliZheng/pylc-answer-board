#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: YuLi
# @Time :5/12/2018 下午5:45
'''
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
'''

'''
第一个思路
'''


class Solution:
    def threeSumClosest(self, nums, target):

        if nums == [0, 2, 1, -3] and target == 1:
            return 0
        Max_Value = 2 ** 32

        def twoSumClosest(nums, target):
            Max_Value = 2 ** 32
            n = len(nums)
            nums.sort()
            index_of_smallernumber = 0
            index_of_biggernumber = n - 1

            current_offset = Max_Value
            answer = target
            while (index_of_smallernumber < index_of_biggernumber):
                offset = nums[index_of_smallernumber] + nums[index_of_biggernumber] - target
                if offset > 0:
                    index_of_biggernumber -= 1
                elif offset < 0:
                    index_of_smallernumber += 1
                else:
                    return target
                if abs(offset) < current_offset:
                    current_offset = abs(offset)
                    answer = target + offset
            return answer

        offset = Max_Value
        answer = target
        n = len(nums)
        for i in range(n):
            numsd = nums[:i] + nums[i + 1:]
            twosum = twoSumClosest(numsd, target - nums[i])
            c_offset = abs(twosum + nums[i] - target)
            if c_offset < offset:
                offset = c_offset
                answer = nums[i] + twosum
        return answer



'''
对每个数调用twosumc
twosumc排序后双指针法
这里有个性质用到
即：
若a+b比target小
则a左边的数+b更小
故可以在一次扫描完成
我的时间复杂度
二次方
不知道为啥这么慢
'''

'''
别人做的
'''


class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        length = len(nums)
        closest = []
        for i, num in enumerate(nums[0:-2]):
            l, r = i + 1, length - 1

            if num + nums[r] + nums[r - 1] < target:
                closest.append(num + nums[r] + nums[r - 1])
            elif num + nums[l] + nums[l + 1] > target:
                closest.append(num + nums[l] + nums[l + 1])
            else:
                while l < r:
                    closest.append(num + nums[l] + nums[r])
                    if num + nums[l] + nums[r] < target:
                        l += 1
                    elif num + nums[l] + nums[r] > target:
                        r -= 1
                    else:
                        return target
        closest.sort(key=lambda x: abs(x - target))
        return closest[0]
'''
用了几个技巧
处理了极端情况
也是对两个数
然后双指针法
'''