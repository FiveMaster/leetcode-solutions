# -*- coding: utf-8 -*-
# @Time    : 2022/3/28 17:25
# @Author  : MasterFive
# @FileName: add_two_numbers.py
# @Software: PyCharm
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = node = ListNode()
        add_label = False
        while True:
            if add_label:
                add = 1
            else:
                add = 0

            if l1 is None:
                l1_val = 0
            else:
                l1_val = l1.val

            if l2 is None:
                l2_val = 0
            else:
                l2_val = l2.val

            if l1_val + l2_val + add < 10:
                node.val = l1_val + l2_val + add
                add_label = False
            else:
                node.val = l1_val + l2_val + add - 10
                add_label = True

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            if l1 is None and l2 is None:
                if add_label:
                    node.next = ListNode(1)
                break
            node.next = ListNode()
            node = node.next
        return p


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    x = Solution().addTwoNumbers(l1, l2)
    while x is not None:
        print(x.val)
        x = x.next
    print("-------")
    l1 = ListNode(0)
    l2 = ListNode(0)
    x = Solution().addTwoNumbers(l1, l2)
    while x is not None:
        print(x.val)
        x = x.next
    print("-------")
    l1 = node1 = ListNode(9)
    node1.next = ListNode(9)
    node1 = node1.next
    node1.next = ListNode(9)
    node1 = node1.next
    node1.next = ListNode(9)
    node1 = node1.next
    node1.next = ListNode(9)
    node1 = node1.next
    node1.next = ListNode(9)
    node1 = node1.next
    node1.next = ListNode(9)
    node1 = node1.next
    l2 = node2 = ListNode(9)
    node2.next = ListNode(9)
    node2 = node2.next
    node2.next = ListNode(9)
    node2 = node2.next
    node2.next = ListNode(9)
    node2 = node2.next
    x = Solution().addTwoNumbers(l1, l2)
    while x is not None:
        print(x.val)
        x = x.next
