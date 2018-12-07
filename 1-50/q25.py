#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: YuLi
# @Time :7/12/2018 下午9:42
'''
给出一个链表，每 k 个节点一组进行翻转，并返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么将最后剩余节点保持原有顺序。
示例 :
给定这个链表：1->2->3->4->5
当 k = 2 时，应当返回: 2->1->4->3->5
当 k = 3 时，应当返回: 3->2->1->4->5
说明 :
你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
'''

'''
第一思路
'''

class Solution:
    def reverseKGroup(self, head, k):
        first=head
        list_store=[]
        list_to_append=[]
        list_to_append_index=0
        while first:
            list_to_append.append(first.val)
            list_to_append_index+=1
            if list_to_append_index==k:
                list_store.extend(list_to_append)
                list_to_append=[]
                list_to_append_index=0
            first=first.next
        length=len(list_store)//k
        for list_reverse_index in range(length):
            start=k*list_reverse_index
            list_store_slice=list_store[start:start+k]
            list_store_reverse=list_store_slice[::-1]
            list_store=list_store[:start]+list_store_reverse+list_store[start+k:]
        list_store+=list_to_append
        res=ListNode(0)
        cur=res
        for val in list_store:
            cur.next=ListNode(val)
            cur=cur.next
        return res.next

'''
我用python自带的slice搞的
'''
'''
我看别人有耍赖的
'''

