#-*-coding:utf-8-*-
if __name__ == '__main__':
    def countsort(li):
        n=len(li)
        k=max(li)
        C=[0]*(k+1)
        for i in li:
            C[i]+=1
        A=[]
        for i in range(k+1):
            if C[i]!=0:
                for j in range(C[i]):
                    A.append(i)

        return A

    li=[6,3,4,5,9,8,7]
    print(countsort(li))