#-*-coding:utf-8-*-

'''
环形链表 II

需要有三个节点

题目：https://leetcode-cn.com/explore/learn/card/linked-list/194/two-pointer-technique/745/


答案：https://blog.csdn.net/sun_white_boy/article/details/82845791

思路：根据相遇点距环入口的距离等于头节点距环入口的距离

结论的计算过程：
https://www.jianshu.com/p/e5db77497cc7

相遇后：此时让慢节点或快节点中的一个指向头节点，另一个留在相遇节点，然后速度都为1，继续遍历链表，双指针再次相遇时的节点刚好是入环节点。
先计算B点，再从头还是计算

官方解析：
https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/linked-list-cycle-ii-kuai-man-zhi-zhen-shuang-zhi-/
'''
class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution():
    def detectCycle(self, head):
        if head is None:
            return
        slow, fast = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                #此时快慢指针相交
                p = head
                #第三个指针从头结点开始
                while p != slow:
                    p = p.next
                    slow = slow.next
                return p

        return None

if __name__ == '__main__':
    head1 = ListNode(3)
    n1 = ListNode(2)
    n2 = ListNode(0)
    n3 = ListNode(-4)
    head1.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n1
    # 这句决定是否有环
    print(Solution().detectCycle(head1))