
#-*-coding:utf-8-*-

'''
计数排序

https://blog.csdn.net/qq_36178641/article/details/80978349

B是排序后的
C是计数
'''
if __name__ == '__main__':

    def su_counting_algorithm(A,B,k):
        #C=range(k+1)
        #python3中range不返回数组对象，而是返回range对象
        # C=list(range(k+1))
        # for i in range(0,k+1):
        #     C[i]=0
        C=[0]*(k+1);
        for j in range(len(A)):
            C[A[j]]=C[A[j]]+1
        for i in range(1,k+1):
            C[i]=C[i]+C[i-1]
        for j in reversed(range(len(A))):
            #把列表从后往前排序
            B[C[A[j]]-1]=A[j]
            C[A[j]]=C[A[j]]-1
        return B

    A=[2,5,3,0,2,3,0,3]
    B=list(range(len(A)))
    print (A)
    print (su_counting_algorithm(A,B,max(A)))
