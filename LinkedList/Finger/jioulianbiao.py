# -*- coding:utf-8 -*-  
'''
function：奇偶链表

给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。

请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。

示例 1:

输入: 1->2->3->4->5->NULL
输出: 1->3->5->2->4->NULL
示例 2:

输入: 2->1->3->5->6->4->7->NULL
输出: 2->3->6->7->1->5->4->NULL
说明:

应当保持奇数节点和偶数节点的相对顺序。
链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推

题目：https://leetcode-cn.com/explore/learn/card/linked-list/195/classic-problems/753/

答案：https://leetcode-cn.com/problems/odd-even-linked-list/solution/jian-dan-zhi-guan-by-lkj5432/

'''

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        if not head:
            return head
        p=head
        t=q=p.next
        while q and q.next:
            p.next,q.next=p.next.next,q.next.next
            p,q=p.next,q.next
        p.next=t
        return head

    # 自己写的例题改编
    def oddEvenList2(self, head):
        if head is None:
            return
        odd = head
        even = evenHead = head.next
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = evenHead
        return head