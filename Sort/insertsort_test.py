#-*-coding:utf-8-*-
if __name__ == '__main__':
    def mergesort(li):
        n=len(li)
        for i in range(1,n):
            j=i
            while j>=1:
                if li[j]<li[j-1]:
                    li[j],li[j-1]=li[j-1],li[j]
                j=j-1
        return li


    li=[99, 22, 64, 55, 11, 35, 89, 1, 2]
    print(mergesort(li))