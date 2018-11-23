#-*-coding:utf-8-*-

if __name__ == '__main__':
   def mergesort(li):
       def adjustheap(li,start,end):
           son=start*2+1
           temp=li[start]
           while son<=end:
                if son<end and li[son]<li[son+1]:
                   son=son+1
                if li[son]<temp:
                    break
                li[start] = li[son]
                start = son
                son = son * 2 + 1
           li[start] = temp

       n=len(li)
       root=n//2-1
       if n<=1:
           return li
       while root>=0:
        adjustheap(li,root,n-1)
        root-=1

        i=n-1
        while i>=1:
            li[0],li[i]=li[i],li[0]
            i-=1
            adjustheap(li,0,i)
        return li

   li=[5, 6, 3, 2, 1, 65, 2, 0, 8, 0]
   print(mergesort(li))

