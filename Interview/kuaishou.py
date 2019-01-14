#-*-coding:utf-8-*-
'''
将n个已经排好序（升序）的数组（数组内存放的是int类型的数字）合并成

一个数组，并且保证合并后的数组仍然是有序的

解题思路：
这道题是二维数组进行排序，用的合并递归

答案
https://blog.csdn.net/Manson_Wang/article/details/82346768



'''
#采用归并排序算法
#拆解到最后，实际变成两个数组进行排序
def MergeSort(nums):
    #请牢记传入的参数是多维数组
    #此处是递归结束条件
    print(nums)
    if len(nums) <= 1:
        return nums
    #取中间位置 
    mid = len(nums) // 2
    print("mid:",mid)
    #此处实现递归
    #记住此处得到的也是多维数组
    print("left:", nums[:mid])
    print("right:", nums[mid:])
    Left = MergeSort(nums[:mid])

    Right = MergeSort(nums[mid:])

    print("Left[0], Right[0]",Left[0], Right[0])
    # 要传入的参数是数组中第一个索引处的值
    #与普通归并排序的特别之处
    return Sort_list(Left[0], Right[0])

def Sort_list(Left, Right):
    #存储排序后的值
        res = []
        while 0 < len(Left) and 0 < len(Right):
            if Left[0] < Right[0]:
                res.append(Left.pop(0))
            else:
                res.append(Right.pop(0))
            #因为存在一个到终点后，另一个还没到终点
            #这时就需要将没到终点的剩下的值添加到数组中
        res +=Left
        res += Right

        #将一维数组二维化
        print("第一次res:", res)
        # 与普通归并排序的特别之处
        res = [res]
        print("第二次res:", res)

        return res

if __name__ == '__main__':
    b = MergeSort([[1,2,3],[2,3,5],[6,7,9],[7,8,9],[3,5,6]])
    print(b)
    #下一步是为了二维变一维
    result = [i for i in b[0]]
    print(result)


# if __name__ == '__main__':
#     s =[[2, 4, 5],
#         [1, 3, 6],
#         [7, 8, 9]
#     ]
