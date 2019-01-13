#-*-coding:utf-8-*-
def set_passline(passline):
    def cmp(val):
        if val >= passline:
            print("Pass")
        else:
            print("Failed")
    return cmp

if __name__ == '__main__':

    f_100 = set_passline(60) #是一个函数cmp
    print(type(f_100))
    print(f_100.__closure__) #闭包是passline = 60
    f_100(89)
    f_100(59)
