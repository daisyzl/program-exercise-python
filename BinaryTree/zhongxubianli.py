# -*- coding:utf-8 -*-  
'''
function：中序遍历二叉树

给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

题目：https://leetcode-cn.com/explore/learn/card/data-structure-binary-tree/2/traverse-a-tree/2/
答案包含三种遍历方法：
https://www.cnblogs.com/ACStrive/p/11222390.html
'''

class TreeNode(object):
    """ Definition of a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # 迭代方法
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []

        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmp = stack.pop()
                res.append(tmp.val)
                root = tmp.right
        return res

    # 递归方法 ，对等于下面的方法
    def inorderTraversal2(self, root):
        res=[]
        if root:
            res+=self.inorderTraversal(root.left)
            res.append(root.val)
            res+=self.inorderTraversal(root.right)
        return res

    def inorderTraversal3(self, root):
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)




if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    print(Solution().inorderTraversal(n1))