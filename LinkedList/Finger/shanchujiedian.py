#-*-coding:utf-8-*-

'''
删除链表的倒数第N个节点

这道题和合并两个有序链表联系起来学习

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
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        new_list = ListNode(0)
        #增加一个新的节点是为了解决head=1，n=1的情况
        pre = new_list
        slow = fast = pre
        pre.next = head
        for i in range(n):
            fast = fast.next
        while fast.next:
        #注意循环的条件是p1.next
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return new_list.next

    #下面是我自己写的，不用新增new_list，但是写错了
    def deleteNode1(self,head,n):
        fast ,slow = head, head
        for i in range(n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return head





if __name__ == '__main__':
    head1 = ListNode(0)
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    head1.next = n1
    n1.next = n2
    n2.next = n3
    result = Solution().removeNthFromEnd1(head1, 1)
    while result != None:
        print(result.val)
        result = result.next