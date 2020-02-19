#-*-coding:utf-8-*-

'''
删除排序数组中的重复项


题目：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/

答案：https://blog.csdn.net/qq_17550379/article/details/80491294

给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:

给定数组 nums = [1,1,2],

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,0,1,1,1,2,2,3,3,4],

函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

你不需要考虑数组中超出新长度后面的元素。
说明:

为什么返回数值是整数，但输出的答案是数组呢?

请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

// nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}


'''
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # print(set(nums))
        # return len(list(set(nums)))



   #这道题的错误在于如果从前往后遍历，有可能把一些元素已经删除了，无法遍历到原先的最后一个元素
        #只有从后往前遍历，即使删除了其它元素，也有第一个元素

    #方法一 错误，但是原因要明确
        n = len(nums)
        print(n)
        result = []
        for i in range(n-1):
            print(i)
            print(nums[i+1])
            print(nums[i])
            if nums[i] == nums[i+1]:
                result.append(nums.pop(i))
        return result

    #方法二
    def removeDuplicates2(self, nums):
        n = len(nums)
        return n - len([nums.pop(i) for i in range(n-1, 0, -1) if nums[i] == nums[i-1]])
    #注意用range的倒序第二个为nums[1]，一定要从后往前
    for i in range(10-1, -1 , -1):
        print(i)
    #注意这样写range可以访问到nums[0]
if __name__ == '__main__':

    nums = [0,0,1,1,1,2,2,3,3,4]
    nums2 =[1,1,2]
    print(Solution().removeDuplicates2(nums))
