#-*-coding:utf-8-*-
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
            self.head = self.Node(val,None)
        else:
            self.head = self.Node(val, self.head)
        self.length +=1



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
            while temp.next is  not None:
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
        if self.length == index:
            self.addAtTail(val)
        elif self.length < index or self.length == 0:
            return
        else:
            temp = self.head
            for i in range(index):
                if i == index-1:
                    temp.next = self.Node(val, temp.next)
                else:
                    temp =temp.next
        self.length +=1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if self.length <= index or self.head is None:
            return
        else:
            temp = self.head
            for i in range(index):
                if i == index-1:
                    temp.next = temp.next.next
                else:
                    temp = temp.next
        self.length -=1


    class Node():
        def __init__(self, val, next):
            self.val = val
            self.next = next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
if __name__ == '__main__':
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
    # 链表变为1-> 2-> 3
    temp = linkedList.head
    while temp is not None:
        print(temp.val)
        temp = temp.next
    linkedList.deleteAtIndex(1)
    temp = linkedList.head
    while temp is not None:
        print(temp.val)
        temp = temp.next
        #现在链表是1-> 3