#-*-coding:utf-8-*-

'''
环形链表 II

题目：https://leetcode-cn.com/explore/learn/card/linked-list/194/two-pointer-technique/745/

答案：https://blog.csdn.net/sun_white_boy/article/details/82845791

思路：根据相遇点距环入口的距离等于头节点距环入口的距离

'''
class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution():
    def detectCycle(self, head):
        if head is None:
            return
        slow, fast = head
        while fast.next.next != None and fast.next != None:
            if fast == slow:
                p = head
                while p.next != slow.next:
                    p = p.next
                    slow =slow.next
                return p.next
        return None