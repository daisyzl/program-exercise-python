#-*-coding:utf-8-*-

'''
堆排序
https://www.cnblogs.com/chengxiao/p/6129630.html

https://blog.csdn.net/aiya_aiya_/article/details/79846380
'''

def  HeapSort(ls):
    def heapadjust(arr,start,end):  #将以start为根节点的堆调整为大顶堆
        temp=arr[start]
        son=2*start+1
        while son<=end:
            if son<end and arr[son]<arr[son+1]:  #找出左右孩子节点较大的
                son+=1
            if temp>=arr[son]:       #判断是否为大顶堆,如果子节点大于父节点，将子节点值赋给父节点（不用进行交换）
                break
            arr[start]=arr[son]     #子节点上移
            start=son                     #继续向下比较
            son=2*son+1
        arr[start]=temp             #将原堆顶插入正确位置
#######
    n=len(ls)
    if n<=1:
        return ls
    #建立大顶堆
    root=n//2-1    #最后一个非叶节点（完全二叉树中）,从第一个非叶子结点从下至上，从右至左调整结构
    while(root>=0):
        heapadjust(ls,root,n)
        root-=1
    #掐掉堆顶后调整堆
    i=n-1
    while(i>=0):
        (ls[0],ls[i])=(ls[i],ls[0])  #将大顶堆堆顶数放到最后
        heapadjust(ls,0,i-1)    #调整剩余数组成的堆
        i-=1
    return ls
#########
if __name__ == '__main__':

    # x=input("请输入待排序数列：\n")
    # y=x.split()
    # arr=[]
    # for i in  y:
    #     arr.append(int(i))
    arr=[0,2,1,3,4,5,6,7,8,9,10,11,12,13,14]
    arr=HeapSort(arr)
    #print(arr)
    print("数列按序排列如下：")
    for i in arr:
        print(i,end=' ')
