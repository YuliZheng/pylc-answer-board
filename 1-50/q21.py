#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: YuLi
# @Time :5/12/2018 下午5:09
'''
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
'''



'''
别人写的
'''

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res=ListNode(0)
        pre=res

        while l1 and l2:
            if l1.val<l2.val:
                pre.next=l1
                l1=l1.next
            else:
                pre.next=l2
                l2=l2.next
            pre=pre.next
        if l1:  #这里直接把l1后续的第一个节点给pre就行了
            pre.next = l1
        elif l2:
            pre.next = l2

        return res.next

'''
没看出和我区别在哪
'''

'''
我写的
'''
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
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
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
