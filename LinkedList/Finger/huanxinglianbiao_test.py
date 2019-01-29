#-*-coding:utf-8-*-

class ListNode():
    def __init__(self, val):
        self.val = val
        self.next =None

class Solution():
    def hasCycle(self, head):
        if head == None:
            return None
        fast, slow = head, head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
