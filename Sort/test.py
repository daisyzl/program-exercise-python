#-*-coding:utf-8-*-
import sys

if __name__ == '__main__':
    t = int(input())
    n, k = [int(i) for i in input().split()]
    for _ in range(t):
        nums = input().split()
        print(nums)
        s = nums[:2 * n]
        for _ in range(k):
            nums[::2], nums[1::2] = nums[:n], nums[n:]
            print(nums[::2])
        print(' '.join(s))
        # n = int(nums[-2])
        # k = int(nums[-1])


