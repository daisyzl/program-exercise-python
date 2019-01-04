#-*-coding:utf-8-*-



class Solution:



    def nextPermutation(self, nums):


        n = len(nums)
        for i in range(n - 1, 0, -1):
            if nums[i] < nums[i - 1]:
                continue
            else:
                min_index = i
                for j in range(i , n-1):
                    if nums[j] < nums[min_index] and nums[j]>nums[i-1]:
                        min_index = j
                    else:
                        continue
                nums[i-1], nums[min_index] = nums[min_index], nums[i-1]
                nums=nums[:i]+sort_test(nums[i:])
                print(nums)
                return nums

def sort_test(arr):
    n = len(arr)
    print("33333")
    print(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
    print(arr)
    return arr






if __name__ == '__main__':
    nums=[1,5,8,4,7,6,5,3,1]

    test=Solution().nextPermutation(nums)
    print(test)
