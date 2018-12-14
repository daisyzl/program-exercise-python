#-*-coding:utf-8-*-
from random import randint

if __name__ == '__main__':
    def heapsort(A,start,end):
        if start>=end:
            return
        temp=A[start]
        left=start
        right=end

        while left<right:
            while left<right and temp<A[right]:
                right-=1
            A[left]=A[right]
            while left<right and temp>A[left]:
                left+=1
            A[right]=A[left]
        A[left]=temp
        heapsort(A,0,left-1)
        heapsort(A,left+1,end)



    li=[6,3,4,5,9,8,7]
    end=len(li)-1
    print(heapsort(li,0,end))
    print(li)

