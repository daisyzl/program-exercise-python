#-*-coding:utf-8-*-
'''
题目描述
牛牛想尝试一些新的料理，每个料理需要一些不同的材料，问完成所有的料理需要准备多少种不同的材料。

输入描述:
每个输入包含 1 个测试用例。每个测试用例的第 i 行，表示完成第 i 件料理需要哪些材料，各个材料用空格隔开，输入只包含大写英文字母和空格，输入文件不超过 50 行，每一行不超过 50 个字符。

输出描述:
输出一行一个数字表示完成所有料理需要多少种不同的材料。

示例1

输入
BUTTER FLOUR
HONEY FLOUR EGG

输出
4
'''
import sys

if __name__ == '__main__':

    sourceslist = []
    for line in sys.stdin:
        needline = line.split()
        #返回分割后的字符串列表,默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等,针对字符串
        sourceslist.extend(needline)

    print(len(set(sourceslist)))

#py.3中input（）只能输入一行  sys.stdin按下换行键然后ctrl+d程序结束

#sys.stdin.readline( )会将标准输入全部获取，包括末尾的'\n'，因此用len计算长度时是把换行符'\n'算进去了的，但是input( )获取输入时返回的结果是不包含末尾的换行符'\n'的。

#因此如果在平时使用sys.stdin.readline( )获取输入的话，不要忘了去掉末尾的换行符，可以用strip( )函数（sys.stdin.readline( ).strip('\n')）或sys.stdin.readline( )[:-1]这两种方法去掉换行。