#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: YuLi
# @Time :5/12/2018 下午5:16
'''
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：
给定的 n 保证是有效的。
进阶：
你能尝试使用一趟扫描实现吗？
'''


'''
我的第一个思路
'''

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        p=head
        newhead=ListNode(0)
        newhead.next=head
        formernode=newhead
        for i in range(n):
            p=p.next
        while not p==None:
            p=p.next
            formernode=formernode.next
        formernode.next=formernode.next.next
        return newhead.next
