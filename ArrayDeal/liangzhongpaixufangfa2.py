#-*-coding:utf-8-*-
'''
题目描述
考拉有n个字符串字符串，任意两个字符串长度都是不同的。考拉最近学习到有两种字符串的排序方法： 1.根据字符串的字典序排序。例如：
"car" < "carriage" < "cats" < "doggies < "koala"
2.根据字符串的长度排序。例如：
"car" < "cats" < "koala" < "doggies" < "carriage"
考拉想知道自己的这些字符串排列顺序是否满足这两种排序方法，考拉要忙着吃树叶，所以需要你来帮忙验证。

输入描述:
输入第一行为字符串个数n(n ≤ 100)
接下来的n行,每行一个字符串,字符串长度均小于100，均由小写字母组成

输出描述:
如果这些字符串是根据字典序排列而不是根据长度排列输出"lexicographically",

如果根据长度排列而不是字典序排列输出"lengths",

如果两种方式都符合输出"both"，否则输出"none"

这道题主要是学习这种编程思路

示例1
输入
3
a
aa
bbb

输出
both
'''
import sys

if __name__ == '__main__':
    data=sys.stdin.readlines()
    flag1=False
    flag2=False
    a=[]
    for i in range(1,int(data[0])+1):
        a.append(data[i])
    if a==sorted(a):#sorted默认按照字符串的字典顺序排序，不能用x.sort（）因为会在原数组中进行更改
        flag1=True
    if a==sorted(a,key=len):
        flag2=True

    if flag1 and flag2:
        print("both")
    elif flag1:
        print("lexicographically")
    elif flag2:
        print("lengths")
    else:
        print("none")