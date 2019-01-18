#-*-coding:utf-8-*-
'''
 反转链表

 思想：迭代方法

 题目：https://leetcode-cn.com/explore/learn/card/linked-list/195/classic-problems/750/

 答案：https://www.cnblogs.com/songzhenhua/p/9652292.html


'''

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution():
        def reverseList(self, head):
            pre = head
            cur = pre.next
            pre.next = None
            #将原链表的第一个节点变成了新链表的最后一个节点，
            # 同时将原链表的第二个节点保存在cur中
            while cur:
                temp = cur.next
                cur.next = pre
                pre = cur
                cur = temp
            #从原链表的第二个节点开始遍历到最后一个节点，将所有节点翻转一遍
            return pre

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


