#-*-coding:utf-8-*-
'''
对角线遍历

https://blog.csdn.net/zzz_cming/article/details/81035354

https://leetcode-cn.com/explore/learn/card/array-and-string/199/introduction-to-2d-array/774/




'''

if __name__ == '__main__':
    A = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

    n = len(A)
    for i in range(n + n - 1):
        for j in range(i + 1):
            k = i - j
            if k < n and k >= 0 and j < n:
                print("对应索引j,k,i:", j, k, i, "     对应值:", A[j][k])


