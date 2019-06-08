import itertools
'''
组合（combination）是一个数学名词。一般地，从n个不同的元素中，任取m（m≤n）个元素为一组，
叫作从n个不同元素中取出m个元素的一个组合。我们把有关求组合的个数的问题叫作组合问题。

种数：m!/((n!)*(m-n)!)
'''

mylist = list(itertools.combinations([1,2,3,4],3))
print(mylist)
print(len(mylist))