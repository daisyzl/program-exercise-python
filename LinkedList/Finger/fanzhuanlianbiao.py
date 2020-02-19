#-*-coding:utf-8-*-
'''
反转链表

思想：迭代方法

反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

题目：https://leetcode-cn.com/explore/learn/card/linked-list/195/classic-problems/750/

答案：https://www.cnblogs.com/songzhenhua/p/9652292.html

有动画比较好理解
https://leetcode-cn.com/problems/reverse-linked-list/solution/dong-hua-yan-shi-206-fan-zhuan-lian-biao-by-user74/

'''

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution():
        def reverseList(self, head):
            if not head:
                return
            pre = head
            cur = pre.next
            pre.next = None
            #将原链表的第一个节点变成了新链表的最后一个节点，
            # 同时将原链表的第二个节点保存在cur中
            while cur:
                temp = cur.next
                cur.next = pre
                #第一和第二之间的交换
                pre = cur
                cur = temp
                #其他三行是第二 和第三往前进一位
            #从原链表的第二个节点开始遍历到最后一个节点，将所有节点翻转一遍
            return pre

        # 此方法比较好理解，双指针
        def reverseList2(self, head):
            # 申请两个节点，pre和 cur，pre指向None
            pre = None
            cur = head
            # 遍历链表，while循环里面的内容其实可以写成一行
            # 这里只做演示，就不搞那么骚气的写法了
            while cur:
                # 记录当前节点的下一个节点
                tmp = cur.next
                # 最后一个节点的next为None
                # 然后将当前节点指向pre
                cur.next = pre
                # pre和cur节点都前进一位
                pre = cur
                cur = tmp
            return pre

        # 迭代方法
        def reverseList3(self, head):
            """
            :type head: ListNode
            :rtype: ListNode
            """
            # 递归终止条件是当前为空，或者下一个节点为空
            if (head == None or head.next == None):
                return head
            # 这里的cur就是最后一个节点
            cur = self.reverseList(head.next)
            # cur也是链表
            # 这里请配合动画演示理解
            # 如果链表是 1->2->3->4->5，那么此时的cur就是5
            # 而head是4，head的下一个是5，下下一个是空
            # 所以head.next.next 就是5->4
            head.next.next = head
            # 防止链表循环，需要将head.next设置为空
            head.next = None
            # 每层递归函数都返回cur，也就是最后一个节点
            return cur

        def reverseList4(self, head):
            """
            :type head: ListNode
            :rtype: ListNode
            """
            # 递归终止条件是当前为空，或者下一个节点为空
            if (head == None or head.next == None):
                return head
            # 这里的cur就是最后一个节点
            cur = self.reverseList(head.next)
            # cur也是链表
            # 这里请配合动画演示理解
            # 如果链表是 1->2->3->4->5，那么此时的cur就是5
            # 而head是4，head的下一个是5，下下一个是空
            # 所以head.next.next 就是5->4
            head.next.next = head
            # 防止链表循环，需要将head.next设置为空
            head.next = None
            # 每层递归函数都返回cur，也就是最后一个节点
            return cur


if __name__ == '__main__':
    head1 = ListNode(0)
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    head1.next = n1
    n1.next = n2
    n2.next = n3
    result = Solution().reverseList3(head1)
    while result != None:
        print(result.val)
        result = result.next


