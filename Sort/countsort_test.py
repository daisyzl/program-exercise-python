#-*-coding:utf-8-*-
if __name__ == '__main__':
    def heapsort(A,n):
        B=[0]*n
        for i in range(len(A)):
            B[A[i]]+=1
        for i in range(1,n):
            B[i]=B[i]+B[i-1]
        C=[0]*len(A)
        for i in range(len(A)):
            C[B[A[i]]-1]=A[i]
            B[A[i]]-=1
        return C






    li=[6,3,4,5,9,8,7]
    n=max(li)
    print(heapsort(li,n+1))