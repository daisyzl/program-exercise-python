#-*-coding:utf-8-*-
'''
二分查找
mid=(low+high)/2, 即mid=low+1/2*(high-low);

插值查找
通过类比，我们可以将查找的点改进为如下：
mid=low+(key-a[low])/(a[high]-a[low])*(high-low)
将上述的比例参数1/2改进为自适应的，
根据关键字在整个有序表中所处的位置，
让mid值的变化更靠近关键字key，
这样也就间接地减少了比较次数。

有序查找

思想
https://blog.csdn.net/weixin_39241397/article/details/79344179

http://python.jobbole.com/87440/

时间复杂度O(log(n))

'''

def insertSearch(nums,target):
    if len(nums)==0:
        return -1
    left,right=0,len(nums)
    while left<right:
        mid=left+(right-left)*(target-nums[left])/(nums[right]-nums[left])
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            right=mid
        else:
            left=mid+1
    if nums[left]==target and len(nums)!=left:
        return left
    return -1

if __name__=='__main__':
    nums=[1, 5, 7, 8, 22, 54, 99, 123, 200, 222, 444]
    print(insertSearch(nums, 123))
