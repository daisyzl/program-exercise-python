#-*-coding:utf-8-*-
'''
版本号大小,字符串


设计思想：
1.使用正则表达式判断版本号格式是否正确
2.将字符串用”.”分隔成数组
3.比较数组长度，将长度短的数组用“0”补齐成相等长度数组
4.逐个遍历数组元素，比较大小


测试用例：
1.版本号为空
2.版本号含非数字
3.版本号长度不一致
4.版本号以点为分隔，逐位比较

'''

import re


def versionCompare(v1, v2):
    v1_check = re.match("\d+(\.\d+){0,2}", v1)
    v2_check = re.match("\d+(\.\d+){0,2}", v2)
    #不符合返回none,符合用group()返回对应的字符串

    if v1_check is None or v2_check is None or v1_check.group() != v1 or v2_check.group() != v2:
        return "版本号格式不对，正确的应该是x.x.x,只能有3段"
    result=v1_check.group()
    print(type(result))
    v1_list = v1.split(".")
    v2_list = v2.split(".")
    v1_len = len(v1_list)
    v2_len = len(v2_list)
    if v1_len > v2_len:
        for i in range(v1_len - v2_len):
            v2_list.append("0")
    elif v2_len > v1_len:
        for i in range(v2_len - v1_len):
            v1_list.append("0")
    else:
        pass
    for i in range(len(v1_list)):
        if v1_list[i] > v2_list[i]:
            return "v1大"
        if v1_list[i] < v2_list[i]:
            return "v2大"
    return "相等"

if __name__ == '__main__':

    # 测试用例
    print(versionCompare(v1="", v2=""))
    print(versionCompare(v1="1.0.a", v2="d.0.1"))
    print(versionCompare(v1="1.0.3", v2="1.0.1"))
    print(versionCompare(v1="1.0.2", v2="1.0.1"))
    print(versionCompare(v1="1.0.1", v2="1.0.2"))
    print(versionCompare(v1="1.0.11", v2="1.0.2"))