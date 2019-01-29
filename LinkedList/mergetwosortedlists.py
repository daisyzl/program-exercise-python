#-*-coding:utf-8-*-
'''
打卡时间：2019.01.15

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
        #这里一定要有pre = new_list ，pre指针指向链表的最后一个，new_list指向head，最后返回可以new_list.next中把0节点删除
        while l1 is not None and l2 is not None:
            #while l1 and l2: 这样子不会报错
            #while l1.val and l2.val: 会报错  'NoneType' object has no attribute 'val'

            if l1.val < l2.val:
                pre.next = l1
                l1 = l1.next
                #循环的时候别忘了这一步
            else:
                pre.next = l2
                l2 = l2.next
            pre = pre.next
            #注意这段不要忘了
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
    while result:
        print(result.val)
        result=result.next


