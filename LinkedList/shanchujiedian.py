#-*-coding:utf-8-*-

'''
删除链表的倒数第N个节点

题目：https://leetcode-cn.com/explore/learn/card/linked-list/194/two-pointer-technique/747/

答案：https://blog.csdn.net/iyuanshuo/article/details/79600168

给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？

'''

class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        if head.next == None:
            return []
        else:
            A = head
            B = head
            for i in range(n):
                A = A.next
            if A == None:
                return head.next
            while A.next:
                A = A.next
                B = B.next
            B.next = B.next.next
        return head

    def removeNthFromEnd2(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        p1 = p2 = dummy
        for i in range(n):
            p1 = p1.next
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
        return dummy.next

    def removeNthFromEnd3(self, head, n):
        p = head
        q = head
        index = 0
        while index != n:
            p = p.next
            index += 1
        if p == None:
            return head.next
        while p.next != None:
            p = p.next
            q = q.next
        q.next = q.next.next
        return head



if __name__ == '__main__':
    head1 = ListNode(0)
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    head1.next = n1
    n1.next = n2
    n2.next = n3
    result = Solution().removeNthFromEnd3(head1, 2)
    while result != None:
        print(result.val)
        result = result.next