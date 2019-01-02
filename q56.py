#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: YuLi
# @Time :2/1/2019 下午4:30
'''
给出一个区间的集合，请合并所有重叠的区间。
示例 1:
输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:
输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
'''
'''
我就一个一个合并
'''
class Solution:
    def merge(self, intervals):
        intervals.sort(key = lambda x : x.start)
        i = 0
        while i < len(intervals)-1:
            f = intervals[i]
            g = intervals[i+1]
            if g.start <= f.end:
                f.end = max(f.end,g.end)
                intervals.pop(i+1)
            else:
                i += 1
        return intervals