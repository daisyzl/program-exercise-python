#-*-coding:utf-8-*-
'''
合并两个有序链表

非递归方法

题目：
https://leetcode-cn.com/problems/merge-two-sorted-lists/

解题思路
https://www.cnblogs.com/yqpy/p/9545645.html


将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4


'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None
        new_list = ListNode(0)
        pre = new_list
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            pre = pre.next
        #l2已经全部排序只剩l1
        if l1 is not None:
            pre.next = l1
        else:
            pre.next = l2
        return new_list.next

if __name__ == '__main__':
    head1 = ListNode(2)
    n1 = ListNode(3)
    n2 = ListNode(4)
    n3 = ListNode(9)
    head1.next = n1
    n1.next = n2
    n2.next = n3

    head2 = ListNode(3)
    m1 = ListNode(5)
    m2 = ListNode(7)
    m3 = ListNode(8)
    head2.next = m1
    m1.next = m2
    m2.next = m3

    result=Solution().mergeTwoLists(head1,head2)
    while result.next is not None:
        print(result.val)
        result=result.next

