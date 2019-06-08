#汉罗塔
def move(n,a,b,c):
    if not isinstance(n,int):
        return TypeError('n is not integer')    #不是整数就返回错误
    if n == 1:
        print(a,'-->',c)                        #如果只有一个就直接从a搬到c
    if n>1 :                                    #大于一个就先把a搬到b,然后再从b搬到c  运用函数的递归思想，从高依次实现
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
move(5,'A','B','C')                   #Test!!



