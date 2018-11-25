#-*-coding:utf-8-*-
from random import randint

if __name__ == '__main__':
    def heapsort(A):
        for i in range(len(A)-1):
            for j in range(1,len(A)-1-i):
                if A[j]<A[j-1]:
                    A[j],A[j-1]=A[j-1],A[j]

        return A









    li=[randint(1,999) for i in range(10)]

    print(heapsort(li))
