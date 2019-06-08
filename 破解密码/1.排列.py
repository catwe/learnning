import itertools


'''
排列，一般地，从n个不同元素中取出m（m≤n）个元素，按照一定的顺序排成一列，叫做从n个元素中取出m个元素的一个排列(permutation)。特别地，当m=n时，这个排列被称作全排列(all permutation)。
中文名 排列 外文名 permutation 定 义 有限集的子集按某种条件的排序包含选排
'''

'''
排列的可能性次数公式 :  n!/(n-m)!
'''
mylist = list(itertools.permutations([1,2,3,4],3))
print(mylist)
print(len(mylist))