#-*-coding:utf-8-*-
'''
单链表

https://leetcode-cn.com/explore/learn/card/linked-list/193/singly-linked-list/741/

设计链表的实现。您可以选择使用单链表或双链表。单链表中的节点应该具有两个属性：val 和 next。val 是当前节点的值，
next 是指向下一个节点的指针/引用。如果要使用双向链表，则还需要一个属性 prev 以指示链表中的上一个节点。
假设链表中的所有节点都是 0-index 的。

在链表类中实现这些功能：

get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val  的节点。如果 index 等于链表的长度，
则该节点将附加到链表的末尾。如果 index 大于链表长度，则不会插入节点。
deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。

示例：

MyLinkedList linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1,2);   //链表变为1-> 2-> 3
linkedList.get(1);            //返回2
linkedList.deleteAtIndex(1);  //现在链表是1-> 3
linkedList.get(1);            //返回3


提示：

所有值都在 [1, 1000] 之内。
操作次数将在  [1, 1000] 之内。
请不要使用内置的 LinkedList 库。

解题答案：
https://unclegem.cn/2018/08/13/Leetcode%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0-707-%C2%9A%E8%AE%BE%E8%AE%A1%E9%93%BE%E8%A1%A8/

'''
class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.length = 0
        self.head = None

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if self.length <= index or self.head is None:
            return -1
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp.val



    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        if self.head is None:
            self.head = self.Node(val, None)
        else:
            self.head = self.Node(val, self.head)
        self.length += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        if self.head is None:
            self.head = self.Node(val, None)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = self.Node(val, None)
        self.length +=1


    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index == 0:
            self.addAtHead(val)
        else:
            if self.length == 0 or self.length < index:
                return
            temp = self.head
            for i in range(index):
                if i == index-1:
                    temp.next = self.Node(val,temp.next)
                else:
                    temp =temp.next
            self.length += 1


    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index == 0:
            self.head == self.head.next
            self.length -= 1

        else:
            if index < self.length:
                temp = self.head
                for i in range(index):
                    if i == index-1:
                        temp.next = temp.next.next
                    temp = temp.next
                    self.length -= 1





    class Node:
        def __init__(self, val, next):
            self.val = val
            self.next= next


if __name__ == '__main__':

        # Your MyLinkedList object will be instantiated and called as such:
        # obj = MyLinkedList()
        # param_1 = obj.get(index)
        # obj.addAtHead(val)
        # obj.addAtTail(val)
        # obj.addAtIndex(index,val)
        # obj.deleteAtIndex(index)


        linkedList = MyLinkedList()
        linkedList.addAtHead(1)
        temp = linkedList.head
        while temp is not None:
            print(temp.val)
            temp = temp.next
        # linkedList = linkedList.head
        linkedList.addAtTail(3)
        temp = linkedList.head
        while temp is not None:
            print(temp.val)
            temp = temp.next
        linkedList.addAtIndex(1, 2)
        #链表变为1-> 2-> 3
        temp = linkedList.head
        while temp is not None:
            print(temp.val)
            temp = temp.next
        # linkedList.get(1)
        # linkedList.deleteAtIndex(1)
        # #现在链表是1-> 3
        # linkedList.get(1)
        #返回3
