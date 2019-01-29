#-*-coding:utf-8-*-

class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution():
    def deleteNode(self,head,n):
        fast ,slow = head, head
        for i in range(n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return head

if __name__ == '__main__':
    head1 = ListNode(0)
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    head1.next = n1
    n1.next = n2
    n2.next = n3
    result = Solution().deleteNode(head1, 2)
    while result != None:
        print(result.val)
        result = result.next

