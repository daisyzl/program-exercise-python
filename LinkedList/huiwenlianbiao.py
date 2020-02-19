# -*- coding:utf-8 -*-  
'''
function：回文链表
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true

题目：https://leetcode-cn.com/explore/learn/card/linked-list/195/classic-problems/754/
答案：https://leetcode-cn.com/problems/palindrome-linked-list/solution/hui-wen-lian-biao-by-leetcode/
第三种方法空间复杂度为1，复杂没有算
'''
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # 空间复杂度为n
    def isPalindrome(self, head):
        if head is None:
            return True
        # 链表为空是回文
        vals = []
        cur = head
        while cur:
            vals.append(cur.val)
            cur = cur.next
        return vals == vals[::-1]
