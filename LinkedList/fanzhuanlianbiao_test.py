#-*-coding:utf-8-*-

class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = next


class Solution():
    def reverseList(self, head):
        pre = head
        cur = head.next
        head.next = None
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre
