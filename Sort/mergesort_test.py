#-*-coding:utf-8-*-


if __name__ == '__main__':
    def adjust(ll,lr):
        result=[]
        while(len(ll)>0 and len(lr)>0):
            if ll[0]<lr[0]:
                result.append(ll.pop(0))
            else:
                result.append(lr.pop(0))

        result+=ll
        result+=lr
        return result



    def heapsort(A):
        n=len(A)
        if n<=1:
            return A
        mid=n//2
        left=A[:mid]
        right=A[mid:]

        ll=heapsort(left)
        lr=heapsort(right)

        return adjust(ll,lr)











    li=[6,3,4,5,9,8,7]
    print(heapsort(li))
