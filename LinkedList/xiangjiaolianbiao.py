#-*-coding:utf-8-*-
'''
相交链表

题目：https://leetcode-cn.com/explore/learn/card/linked-list/194/two-pointer-technique/746/

答案：https://blog.csdn.net/gq930901/article/details/81813788

'''

class ListNode():
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution():
    def getIntersectionNode(self, headA, headB):
        lenA , lenB = 0, 0
        pA, pB = headA, headB
        while pA:
            pA = pA.next
            lenA += 1
        while pB:
            pB = pB.next
            lenB += 1
        if lenA > lenB:
            for i in range(lenA - lenB):
                pA = pA.next
        else:
            for i in range(lenB - lenA):
                pB = pB.next
        while pA != pB:
            pA = pA.next
            pB = pB.next
        return pA

