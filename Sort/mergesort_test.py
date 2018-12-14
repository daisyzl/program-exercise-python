#-*-coding:utf-8-*-


if __name__ == '__main__':
    def heapsort(li):
        n=len(li)
        if n<=1:
            return li
        mid=n//2
        left=li[:mid]
        right=li[mid:]
        ll=heapsort(left)
        lr=heapsort(right)
        return adjustsort(ll,lr)

    def adjustsort(ll,lr):
        result=[]
        while len(ll)>0 and len(lr)>0:
            if ll[0]<lr[0]:
                result.append(ll.pop(0))
            else:
                result.append(lr.pop(0))
        result+=ll
        result+=lr
        return result













    li=[6,3,4,5,9,8,7]
    print(heapsort(li))
