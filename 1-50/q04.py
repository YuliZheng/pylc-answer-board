#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: YuLi
# @Time :5/12/2018 下午8:39
'''
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。
示例 1:
nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:
nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5
'''
'''
没做出来放答
'''


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and nums2[j - 1] > nums1[i]:
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                imax = i - 1
            else:
                if i == 0:
                    max_of_left = nums2[j - 1]
                elif j == 0:
                    max_of_left = nums1[i - 1]
                else:
                    max_of_left = max(nums1[i - 1], nums2[j - 1])
                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2.0
'''
对于所有的i
i是第一个数组下标
我们对这样的j
j的和是总数组长度的一半
如果找到了这样的i
那么i左边
和j左边加起来就是一半
只要对所有的i
找到满足左边小于右边就找到了中位
即A[i]<B[j+1]
且B[j]<A[i+1]
但是左边随i递增
j又随i递减
若第一个等式不满足
i--
第二个
i++
用二叉搜索
'''
