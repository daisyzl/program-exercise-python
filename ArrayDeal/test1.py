#-*-coding:utf-8-*-




if __name__ == "__main__":
    s = ["hello", "world","sunshine"]
    # p =[len(i) for i in s ]
    # print(p)
    result = lambda x:max([len(i) for i in x ])
    n =result(s)
    print(n)
    # for i in s:
    #     print(len(list(i)))