#-*-coding:utf-8-*-
import sys

if __name__ == '__main__':
    data=sys.stdin.readlines()
    a=[int(i) for i in data[1].strip().split() ]
    print(a)
    num=int(data[0].strip())

    def sub(a,num):
        aver=sum(a)//num
        print(aver)
        if sum(a)%num!=0:
            return -1
        for i in range(num):
            if abs(a[i]-aver)%2!=0:
                return -1
        cnt=0
        for i in range(num):
            if a[i]>aver:
                print(cnt)
                cnt+=(a[i]-aver)//2
        return cnt

    print(sub(a,num))





