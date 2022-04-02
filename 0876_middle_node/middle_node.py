# -*- coding: utf-8 -*-
# @Time    : 2022/4/2 16:37
# @Author  : MasterFive
# @FileName: middle_node.py
# @Software: PyCharm


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        heads = {}
        index = 0
        while head is not None:
            heads[index] = head
            head = head.next
            index += 1
        return heads[index // 2]


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    res = Solution().middleNode(head)
    print(res.val)



