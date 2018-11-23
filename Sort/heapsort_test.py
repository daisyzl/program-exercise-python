#-*-coding:utf-8-*-
#-*-coding:utf-8-*-

if __name__ == '__main__':
    def mergesort(li):
        def adjustheap(li,start,end):
            son=start*2+1
            temp=li[start]
            while(son<=end):
                if son<end and li[son]<li[son+1]:
                    son=son+1
                if temp>li[son]:
                    break
                li[start]=li[son]
                start=son
                son=son*2+1
            li[start]=temp


        root=len(li)//2-1
        if len(li)<=1:
            return li
        while(root>=0):
            adjustheap(li,root,len(li)-1)
            root-=1

        n=len(li)-1
        while(n>0):
            li[0],li[n]=li[n],li[0]
            n-=1
            adjustheap(li,0,n)
        return li

    li=[99, 22, 64, 55, 11, 35, 89,89, 1, 2]
    print(mergesort(li))