#-*-coding:utf-8-*-
'''
题目描述
“回文串”是一个正读和反读都一样的字符串，
比如“level”或者“noon”等等就是回文串。
花花非常喜欢这种拥有对称美的回文串，
生日的时候她得到两个礼物分别是字符串A和字符串B。
现在她非常好奇有没有办法将字符串B插入
字符串A使产生的字符串是一个回文串。
你接受花花的请求，帮助她寻找有多少种插入
办法可以使新串是一个回文串。如果字符串B插入
的位置不同就考虑为不一样的办法。
例如：
A = “aba”，B = “b”。这里有4种把B插入A的办法：
* 在A的第一个字母之前: "baba" 不是回文
* 在第一个字母‘a’之后: "abba" 是回文
* 在字母‘b’之后: "abba" 是回文
* 在第二个字母'a'之后 "abab" 不是回文
所以满足条件的答案为2

输入描述:
每组输入数据共两行。
第一行为字符串A
第二行为字符串B
字符串长度均小于100且只包含小写字母

输出描述:
输出一个数字，表示把字符串B插入字符串A之后构成一个回文串的方法数

示例1
输入
aba
b

输出
2
'''

if __name__ == '__main__':
    A=list(input())
    B=list(input())
    cnt=0
    for i in range(len(A)):
        #range() 函数可创建一个整数列表，一般用在 for 循环中 range（0， 5） 是[0, 1, 2, 3, 4]没有5
        tmp=A[:i]+B+A[i:]
        print(A[:i])
        if tmp==tmp[::-1]:
            cnt +=1
    tmp=A+B
    if tmp==tmp[::-1]:  #注意思考为什们会多这一层判断
        cnt +=1
    print(cnt)

    '''
    data=sys.stdin.readlines()#这种输入是包含回车符的
    a=data[0].strip()
    print(a)
    print(type(a))

    b=data[1].strip()
    print(b)
    print(type(b))
    cnt=0
    for i in range(len(a)):#直接对字符串操作即可，不用转换成列表
        result=a[:i]+b+a[i:]
        if result==result[::-1]:
            cnt+=1
    if a+b==(a+b)[::-1]:
        cnt += 1
    print(cnt)
    
    
    
    
    '''
