#-*-coding:utf-8-*-
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None or l2 is None:
             return None
        pre = ListNode(0)
        new_list = pre
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                pre.next = ListNode(l1.val)
                # print(pre.val)
                l1 = l1.next
                # print("111111111")
            else:
                pre.next = ListNode(l2.val)
                # print(pre.val)
                l2 = l2.next
                # print("222222222")

            pre = pre.next
        if l1 is None:
            pre.next = l2
            # print("3333333")
        elif l2 is None:
            pre.next = l1
        return new_list.next

if __name__ == '__main__':
    head1 = ListNode(2)
    n1 = ListNode(3)
    n2 = ListNode(4)
    n3 = ListNode(9)
    head1.next = n1
    n1.next = n2
    n2.next = n3

    head2 = ListNode(3)
    m1 = ListNode(5)
    m2 = ListNode(7)
    m3 = ListNode(8)
    head2.next = m1
    m1.next = m2
    m2.next = m3

    result=Solution().mergeTwoLists(head1,head2)
    while result.next is not None:
        # print("dadad")

        result=result.next
        print(result.val)
