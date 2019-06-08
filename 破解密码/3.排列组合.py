import itertools

# repeat = 密码位数
mylist = list(itertools.product('0123456789',repeat=1))
# print(mylist)
print(len(mylist))