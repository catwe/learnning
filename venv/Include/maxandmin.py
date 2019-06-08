print('练习:请使用迭代查找一个list中最小和最大值，并返回一个tuple：')
def findMinAndMax(L):
    if L !=[]:
        (min,max)=(L[0],L[0])
        for x in L:
            if max<x:
                max=x
            if min>x:
                min=x
        return(min,max)
    else:
        return(None,None)




if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')