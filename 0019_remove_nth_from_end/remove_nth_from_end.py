# -*- coding: utf-8 -*-
# @Time    : 2022/4/2 17:05
# @Author  : MasterFive
# @FileName: remove_nth_from_end.py
# @Software: PyCharm


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nodes = {}
        index = 0
        node = head
        while node is not None:
            nodes[index] = node
            node = node.next
            index += 1
        if index - n - 1 >= 0:
            pre_node = nodes[index - n - 1]
            pre_node.next = nodes[index - n].next
            return head
        else:
            return head.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    res = Solution().middleNode(head)
    print(res.val)

