#-*-coding:utf-8-*-
'''
A = [0, 1, 2, 3, 4]
B = [5, 6, 7, 8, 9]

求A+B的偶数列

zip函数接受任意多个可迭代对象作为参数,将对象中对应的元素打包成一个tuple,然后返回一个可迭代的zip对象.

这个可迭代对象可以使用循环的方式列出其元素

若多个可迭代对象的长度不一致,则所返回的列表与长度最短的可迭代对象相同.

https://www.cnblogs.com/renpingsheng/p/7755312.html

'''

class Solution():
    def test(self, A, B):
        result = [sum(i) for i in zip(A, B)][::2]
        print(result)

if __name__ == '__main__':
    A = [0, 1, 2, 3, 4]
    B = [5, 6, 7, 8, 9]

    Solution().test(A, B)
