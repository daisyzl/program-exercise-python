#-*-coding:utf-8-*-

if __name__ == '__main__':
    def heapsort(li):
        def heapadjust(li,start,end):
            temp=li[start]
            son=start*2+1
            while son<=end:
                if son<end and li[son]<=li[son+1]:
                    son=son+1
                if temp>=li[son]:
                    break
                li[start]=li[son]
                start=son
                son=son*2+1
            li[start]=temp

        if len(li)<=1:
            return

        root=len(li)//2-1
        while(root>=0):
            heapadjust(li,root,len(li)-1)
            root-=1

        i=len(li)-1
        while(i>0):
            li[i],li[0]=li[0],li[i]
            heapadjust(li,0,i-1)
            i=i-1
        return li




    li=[0,2,1,3,4,5,6,7,8,9,10,11,12,13,14]
    print(heapsort(li))

