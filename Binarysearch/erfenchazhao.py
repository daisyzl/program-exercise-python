# -*- coding:utf-8 -*-  
'''
function：
'''

class Solution:

    # 递归方法，查找是否有目标值，返回True和False。
    # 如果题目问目标值的下标此解法不合适，因为每次递归数组发生变化，则下标也发生变化
    def search(self, nums, target):
        left, right = 0, len(nums)-1
        if left>right:
            return False
        mid = (left+right)//2
        if nums[mid]<target:
            print("小",nums[mid], target)
            return self.search(nums[mid+1:right+1], target)
        # 数组的第二个值不计算在数组中，注意right+1
        elif nums[mid]>target:
            print("大", nums[mid],target)
            return self.search(nums[left: mid], target)
        else:
            return True

    def sub_search(self, nums, left, right, target):
        if left > right:
            return -1
        mid = (left + right)//2
        if nums[mid] < target:
            return self.sub_search(nums, mid+1, right, target)
        elif nums[mid] > target:
            return self.sub_search(nums, left, mid-1, target)
        else:
            return mid

    # 递归算法，求目标值的下标
    def search1(self, nums, target):
        return self.sub_search(nums, 0, len(nums)-1, target)


    # 使用迭代的思想，效率高一些，优先使用
    def search2(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right)//2
            # 每次循环重新找中点
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # 继续向右查找
                left = mid+1
            else:
                # 继续向左查找
                right = mid-1
        return -1

    def sub_search2(self, nums, left, right, target):
        if left > right:
            return -1
        mid = (left + right)//2
        if nums[mid] < target:
            return self.sub_search2(nums, mid+1, right, target)
        elif nums[mid] > target:
            return self.sub_search2(nums, left, mid-1, target)
        else:
            res = []
            temp = mid-1
            # 向mid索引值左边扫描
            while True:
                if temp < 0 or nums[temp] != target:
                    break
                res.append(target)
                temp -= 1
            res.append(target)
            # 找到的目标中间值
            temp = mid+1
            # 向mid索引值右边扫描
            while True:
                if temp > len(nums)-1 or nums[temp] != target:
                    break
                res.append(target)
                temp += 1
        return res
    # 递归算法，输出目标值连续相同的数组
    def search3(self, nums, target):
        return self.sub_search2(nums, 0, len(nums)-1, target)

if __name__ == '__main__':
    numbers = [1, 2, 7, 9, 11, 15,15]
    target = 15
    result = Solution().search3(numbers, target)
    print(result)
