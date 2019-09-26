#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/24 15:39
# @Author : Zhangmi
# @Site : 
# @File : dxlb.py
# @Software: PyCharm

class SingleListNode(object):
    """单节点类"""
    def __init__(self, _item, _next=None):
        self.item = _item
        self.next = _next


class SingleLinkedList(object):
    """单链表类"""
    def __init__(self):
        self.head = None
        print('hello,cainiao')

    def is_empty(self):
        return self.head is None

    def add(self, newdata):
        node = SingleListNode(newdata, _next=self.head)
        self.head = node

    def append(self, newdata):
        node = SingleListNode(newdata)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, newdata):
        """将newdata插入pos位置之后"""
        if pos <= 0:
            self.add(newdata)
        elif pos > self.length() - 1:
            self.append(newdata)
        else:
            node = SingleListNode(newdata)
            cur = self.head
            count = 0
            while count < pos - 1:
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, olddata):
        """从单链表中删除所有的olddata"""
        cur = self.head
        pre = None
        while cur is not None:
            if cur.item == olddata:
                if not pre:
                    self.head = cur.next
                else:
                    pre.next = cur.next
                cur = cur.next
            else:
                pre = cur
                cur = cur.next

    def length(self):
        """返回单链表的长度"""
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """打印整个单链表
        return
        ------
        ls: list，从前至后的单链表"""
        cur = self.head
        ls = []
        while cur is not None:
            ls.append(cur.item)
            cur = cur.next
        return ls

    def search(self, data):
        cur = self.head
        while cur is not None:
            if cur.item == data:
                return True
            else:
                cur = cur.next
        return False

    def getNode(self):

        if self.head is not None:
            old = self.head
            cur = old.next
            self.head = cur
            return old.item
        else:
            return None
