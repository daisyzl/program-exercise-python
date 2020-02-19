# -*- coding:utf-8 -*-  
'''
function：移除链表元素
删除链表中等于给定值 val 的所有节点。

示例:

输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5

题目：https://leetcode-cn.com/explore/learn/card/linked-list/195/classic-problems/752/
答案：https://leetcode-cn.com/problems/remove-linked-list-elements/solution/yi-chu-lian-biao-yuan-su-by-leetcode/

'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
        sentinel = ListNode(0)
        sentinel.next = head

        prev, curr = sentinel, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return sentinel.next

    # 下面这个是上面的简写，对比删除节点写的
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        p = ListNode(0)
        fast = head
        p.next, head = head, p
        slow = head
        while fast:
            if fast.val == val:
                slow.next = fast.next
            else:
                slow = slow.next
                # 注意这里如果if条件语句成功就已经跳过一个值了
            fast = fast.next
        return head.next


