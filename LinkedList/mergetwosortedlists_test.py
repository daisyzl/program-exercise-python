#-*-coding:utf-8-*-
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    def mergeTwoLists(self, l1, l2):
        if l1 is None and l2 is None:
            return None
        new_list = ListNode(0)
        pre = new_list

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            pre = pre.next
        if l1 is not None:
            pre.next = l1
        else:
            pre.next = l2
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

    result = Solution().mergeTwoLists(head1, head2)
    while result:
        print(result.val)
        result = result.next



