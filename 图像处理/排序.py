while True:
    h = input('请输入一串数字:')
    h_list = list(map(int, list(h)))
    h_list.sort()
    # a=max(h)
    # b=min(h)
    k=h_list[4]
    print('排序后的列表为： %s' % h_list)
    print(k)
    # print('输入列表最大值： %s' %a)
    # print('输入列表最小值： %s' %b)
# [[ 2  1  7  5  8  9  1  3]
#  [ 3  5  1  2  1 10  1  1]
#  [ 1  6  5  6  5  1  1  7]
#  [ 7  1  5  1  5  1  8  1]
#  [ 9  1  1  5  2  5  2  3]
#  [ 1  2  6  3  1  1  8  1]
#  [ 3  6  1  8 12  5  1  9]
#  [ 7  8  3  9  1  7  8  1]]