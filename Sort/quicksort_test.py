#-*-coding:utf-8-*-
from random import randint

if __name__ == '__main__':
    def heapsort(A,start,end):
        if start>=end :
            return A
        temp=A[start]
        left=start
        right=end
        while left<right:
            if left<right and A[right]>temp:
                right-=1
            A[left]=A[right]
            if left<right and A[left]<temp:
                left+=1
            A[right]=A[left]
        A[left]=temp
        heapsort(A,start,left-1)
        heapsort(A,right+1,end)

        return A







    li=[6,3,4,5,9,8,7]
    n=max(li)
    print(heapsort(li,0,len(li)-1))