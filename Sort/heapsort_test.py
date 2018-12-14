#-*-coding:utf-8-*-
#-*-coding:utf-8-*-

if __name__ == '__main__':
    def mergesort(li):
        def adjustsort(li,start,end):
            son=2*start+1
            temp=li[start]
            while son<=end:
                if li[son]<li[son+1] and son<end:
                    son=son+1
                if temp>=li[son]:
                    break

                li[start]=li[son]
                start = son
                son=2*son+1
            li[start]=temp


        n=len(li)
        if n<=1:
            return li
        root=n//2-1
        while root>=0:
            adjustsort(li,root,n-1)
            root-=1

        i=n-1
        while i>0:
            li[0],li[i]=li[i],li[0]
            i-=1
            adjustsort(li,0,i)

        return li

    arr=[4,6,8,5,9]
    print(mergesort(arr))