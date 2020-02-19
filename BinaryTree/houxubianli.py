# -*- coding:utf-8 -*-  
'''
function：
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

'''

class TreeNode(object):
    """ Definition of a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # 迭代方法和前序遍历的迭代方法一起记忆
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []

        while root or stack:
            if root:
                res.append(root.val)
                stack.append(root)
                root = root.right
            else:
                temp = stack.pop()
                root = temp.left
        return res[::-1]
        # 根，右，左

    #递归
    def postorderTraversal2(self, root):
        res = []

        if root:
            res += self.postorderTraversal(root.left)
            res += self.postorderTraversal(root.right)
            res.append(root.val)
        return res


if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    print(Solution().postorderTraversal(n1))