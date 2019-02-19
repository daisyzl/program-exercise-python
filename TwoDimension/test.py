#-*-coding:utf-8-*-

if __name__ == '__main__':
    l1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for i in zip(*l1):
        print(i)
    result = []
    for i in zip(*l1):
        result.append(list(i))

    print(result)

    for i in zip(l1):
        print(i)

    result = [ [j[i] for j in l1]for i in range(len(l1[0]))]
    print(result)
    for i in l1:
        print(i)