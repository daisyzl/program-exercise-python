#-*-coding:utf-8-*-



def heapsort(nums):
    if len(nums)<=1:
        return nums
    left, right = 0, len(nums)
    mid = (left + right)//2
    l = nums[:mid]
    r = nums[mid:]
    l = heapsort(l)
    r = heapsort(r)
    return adjustsort(l, r)

def adjustsort(l,r):
    result = []
    while len(l) > 0 and len(r) > 0:
        if l[0]<=r[0]:
            result.append(l.pop(0))
        else:
            result.append(r.pop(0))

    result += l
    result += r
    return result












if __name__ == '__main__':

    li=[6, 3, 4, 5, 9, 5,  8, 7]
    result = heapsort(li)
    print(result)
