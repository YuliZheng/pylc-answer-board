#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: YuLi
# @Time :7/12/2018 下午9:33
'''
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
示例:
输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
'''

'''
我的思路
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        def mergeTwoLists(l1, l2):
            firsthead = l1
            lasthead = l2
            answer = ListNode(0)
            tail = answer
            while firsthead and lasthead:
                if firsthead.val < lasthead.val:
                    tail.next = firsthead
                    firsthead = firsthead.next
                    tail = tail.next
                else:
                    tail.next = lasthead
                    tail = tail.next
                    lasthead = lasthead.next
            if firsthead != None:
                tail.next = firsthead
            elif lasthead != None:
                tail.next = lasthead
            return answer.next

        if len(lists) == 0:
            return None
        while len(lists) != 1:
            firsthead = lists[0]
            secondhead = lists.pop(1)
            merge = mergeTwoLists(firsthead, secondhead)
            lists[0] = merge
        return lists[0]


'''
这题我是调用合并两表
看别人最快的那些算法都是用了列表来排序
觉得不好
'''