#-*-coding:utf-8-*-
if __name__ == '__main__':
    def mergesort(li):
        n=len(li)
        gap=n//2
        while gap>0:
            for i in range(gap,n):
                j=i
                while j>gap:
                    if li[j]<li[j-gap]:
                        li[j],li[j-gap]=li[j-gap],li[j]
                    j-=gap
            gap=gap//2
        return li




    li=[4,6,8,5,10,9]
    print(mergesort(li))