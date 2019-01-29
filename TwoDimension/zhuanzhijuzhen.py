#-*-coding:utf-8-*-
'''
zip函数接受任意多个可迭代对象作为参数,将对象中对应的元素打包成一个tuple,然后返回一个可迭代的zip对象.

这个可迭代对象可以使用循环的方式列出其元素

若多个可迭代对象的长度不一致,则所返回的列表与长度最短的可迭代对象相同.

https://www.cnblogs.com/renpingsheng/p/7755312.html

'''

class Solution():

    def transpose(self, A):
        R, C = len(A), len(A[0])
        #行数，列数
        result = [[0] * R for i in range(C)]
        #初始化二维数组
        for r, row in enumerate(A):
            print(row)
            '''
           [1, 2, 3]
            [4, 5, 6]
            [7, 8, 9] 
             '''
            for c, val in enumerate(row):
                result[c][r] = val
        return result





if __name__ == '__main__':
    l1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    result = [[j[i] for j in l1] for i in range(len(l1[0]))]
    print(result)

    for i in range(len(l1[0])):
        for j in l1:
            print(j[i])
            print(i)
            #i=0时，输出第一列

    for i in zip(l1):
        print(i)

    '''
    ([1, 2, 3],)
    ([4, 5, 6],)
    ([7, 8, 9],)

    (1, 4, 7)
    (2, 5, 8)
    (3, 6, 9)
    
    zip相当于压缩  zip（*）相当于解压
    '''


    for i in zip(*l1):
         print(i)

    print(Solution().transpose(l1))



