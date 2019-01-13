#-*-coding:utf-8-*-

def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums)-1
    cnt = 0
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        cnt +=1
        print("cnt", cnt)
        print("left,right",left,right)

    return -1
if __name__=='__main__':
    nums = [1, 3, 5, 7, 8]
    print(binarySearch(nums, 7))