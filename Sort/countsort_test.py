#-*-coding:utf-8-*-
if __name__ == '__main__':
    def countsort(li):
        k=max(li)
        n=len(li)
        B=[0]*(k+1)
        for i in li:
            B[i]+=1
        for i in range(1,k+1):
            B[i]=B[i]+B[i-1]
        C=[0]*n
        for i in range(n):
            C[B[li[i]]-1]=li[i]
            B[li[i]]-=1
        return C





    li=[6,3,4,5,9,8,7]
    print(countsort(li))
