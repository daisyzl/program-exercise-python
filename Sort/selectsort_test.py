#-*-coding:utf-8-*-
from random import randint

if __name__ == '__main__':
    def heapsort(A,n):
        for i in range(0,n-1):
            for j in range(i+1,n):
                if A[i]>A[j]:
                    A[i],A[j]=A[j],A[i]
        return A








    li=[randint(1,999) for i in range(10)]
    n=len(li)
    print(heapsort(li,n))