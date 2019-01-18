#-*-coding:utf-8-*-

'''



'''
class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    def reverseList(self, head, pre = None):
        if not head:
            return pre
        cur = head.next
        head.next = pre
        return self.reverseList(cur, head)


