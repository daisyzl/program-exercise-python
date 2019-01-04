#-*-coding:utf-8-*-

'''

实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1


https://leetcode-cn.com/problems/next-permutation/

主要是记住该种思想

'''

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
    # nums=[1,5,8,4,7,6,5,3,1]

    nums=[1,2,3]
    test=Solution().nextPermutation(nums)
    print(test)
