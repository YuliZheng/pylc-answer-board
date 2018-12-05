#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: YuLi
# @Time :5/12/2018 下午9:12
'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        p = l1
        q = l2
        while q is not None:
            p.val = p.val + q.val
            if p.val >= 10:
                p.val -= 10
                if p.next is None:
                    p.next = ListNode(1)
                else:
                    r = p.next
                    while r.val == 9:
                        r.val = 0
                        if r.next is None:
                            r.next = ListNode(0)
                        r = r.next
                    r.val = r.val + 1
            if p.next is not None:
                p = p.next
            elif q.next is not None:
                p.next = ListNode(0)
                p = p.next
            q = q.next
        return l1

'''
每位运算
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        head = ListNode(0)
        head.next = l1
        carry = 0

        while l1 and l2:
            s = l1.val + l2.val + carry
            val, carry = s % 10, s // 10
            l1.val = val
            prev, l1, l2 = l1, l1.next, l2.next

        l = l1 or l2
        prev.next = l
        while l and carry:
            s = l.val + carry
            val, carry = s % 10, s // 10
            l.val = val
            prev, l = l, l.next

        if carry:
            prev.next = ListNode(1)
