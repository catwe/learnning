#杨辉三角
def triangle():
    L = [1]
    while 1:
        yield L    #遇到就返回一次，下次从此处继续执行
        L = [1]+[L[i]+L[i+1] for i in range(len(L)-1)]+[1]
        #L = [1] + [L[i] + L[i + 1] for i in range(len(L) - 1)] + [1]

#test
n = 0
results = []
for t in triangle():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')