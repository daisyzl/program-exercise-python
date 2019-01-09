#-*-coding:utf-8-*-
def test(strs):
    if not strs:
        return ""
    if len(strs)==1:
        return strs
    n=min([len(x) for x in strs])

