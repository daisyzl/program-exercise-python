# -*- coding:utf-8 -*-  
'''
function：二叉树的前序遍历
给定一个二叉树，返回它的 前序 遍历。

 示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,2,3]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

答案：https://leetcode-cn.com/problems/binary-tree-preorder-traversal/solution/er-cha-shu-de-qian-xu-bian-li-by-leetcode/
答案包含三种遍历方法：
https://www.cnblogs.com/ACStrive/p/11222390.html

目前知识积累只复习递归方法

前序，中序，后序遍历步骤
前序遍历：
1.先输出当前节点
2.如果左子节点不为空，则递归继续前序遍历
3.如果右子节点不为空，则递归继续前序遍历

中序遍历：
1.如果左子节点不为空，则递归继续中序遍历
2.输出当前节点
3.如果右子节点不为空，则递归继续中序遍历

后序遍历
1.如果左子节点不为空，则递归继续后序遍历
2.如果右子节点不为空，则递归继续后序遍历
3.输出当前节点

'''
class TreeNode(object):
    """ Definition of a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # 迭代方法
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        # stack相当于分层

        while root or stack:
            if root:
                res.append(root.val)
                stack.append(root)
                root = root.left
                # 先处理根和左子树
            else:
                temp = stack.pop()
                root = temp.right
        return res

    # 递归方法
    def preorderTraversal2(self, root):
        '''递归解法'''
        res = []

        if root:
            res.append(root.val)
            res += self.preorderTraversal(root.left)
            res += self.preorderTraversal(root.right)

        return res


if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    print(Solution().preorderTraversal2(n1))