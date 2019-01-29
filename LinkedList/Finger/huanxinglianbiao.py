#-*-coding:utf-8-*-
'''
环形链表

题目：https://leetcode-cn.com/explore/learn/card/linked-list/194/two-pointer-technique/744/

答案：https://github.com/luliyucoordinate/Leetcode/blob/master/src/0141-Linked-List-Cycle/0141.py
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        slow, fast = head, head
        while fast.next  and fast.next.next:
            #双指针用fast.next
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        return False

if __name__ == '__main__':
    head1 = ListNode(3)
    n1 = ListNode(2)
    n2 = ListNode(0)
    n3 = ListNode(-4)
    head1.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n1
    #这条语句决定有环还是无环
    result = Solution().hasCycle(head1)
    print(result)
