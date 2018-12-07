#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: YuLi
# @Time :7/12/2018 下午9:40
'''
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
示例:
给定 1->2->3->4, 你应该返回 2->1->4->3.
'''


class Solution:
    def swapPairs(self, head):
        prev = ListNode(0)
        prev.next = head
        first = head
        if head is None:
            return head
        if head.next is None:
            return head
        res = head.next
        while (first and first.next):
            second = first.next
            prev.next = second
            first.next = second.next
            second.next = first
            prev = first
            first = prev.next


'''
常规思路
'''
