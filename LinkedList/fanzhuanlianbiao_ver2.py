#-*-coding:utf-8-*-

# -*-coding:utf-8-*-
'''
 反转链表

 思想：递归方法（比较难）

 题目：https://leetcode-cn.com/explore/learn/card/linked-list/195/classic-problems/750/


'''


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution():
    def reverseList(self, head, prev = None):
        if not head:
            return prev
        cur = head.next
        head.next = prev
        return self.reverseList(cur, head)


if __name__ == '__main__':
    head1 = ListNode(0)
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    head1.next = n1
    n1.next = n2
    n2.next = n3
    result = Solution().reverseList(head1)
    while result != None:
        print(result.val)
        result = result.next
