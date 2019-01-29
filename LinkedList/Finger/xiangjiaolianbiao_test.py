#-*-coding:utf-8-*-
class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution():
    def getIntersectionNode(self, headA, headB):
        lenA, lenB = 0, 0
        A = headA
        B = headB
        while A:
            A = A.next
            lenA += 1
        while B:
            B = B.next
            lenB += 1
        A = headA
        B = headB
        if lenA > lenB:
            for i in range(lenA - lenB):
                A = A.next
        else:
            for i in range(lenB - lenA):
                B = B.next

        while A != B:
            A = A.next
            B = B.next
        return A