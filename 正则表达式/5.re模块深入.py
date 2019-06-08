import re

'''
字符串切割

'''
str1 = 'wangcong     is a good man'
print(str1.split( ))
print(re.split(' +',str1))


'''
re.finditer函数
pattern:匹配的正则表达式（格式）
string:要匹配的字符串（输入的字符串）
flags：标志位，用于控制正则表达式的匹配方式
功能：与findall类似，扫描整个字符串，返回的是一个迭代器

'''
str2 = 'wangcong is a good man!wangcong is a good man!wangcong is a good man'
d = re.finditer(r'(wangcong)',str2)
while True:
    try:
        l = next(d)
        print(d)
    except StopIteration as e:
        break


'''
wangcong is a good good good man
字符串替换和修改
sub(pattern, rep1, string, count=0, flags=0)
subn(pattern, rep1, string, count=0, flags=0)
pattern:  正则表达式（规则）
rep1:     指定用来替换的字符
string:   目标字符串
count:    最多替换次数
flags:    标志位，用于控制正则表达式的匹配方式
功能：    在目标字符串中以正则表达式规则匹配字符串，再把他们替换成指定的字符串，
          可以指定替换的次数，不指定就全部替换。
          
区别：     前者返回被替换的字符串，后者返回一个元组，第一个元素是要替换的字符串
'''


str3 = 'wangcong is a good good good man'
# print(re.sub(r'(good)','nice',str3,count=2))
# print(type(re.sub(r'(good)','nice',str3,count=2)))

print(re.subn(r'(good)','nice',str3,))
print(type(re.subn(r'(good)','nice',str3,count=2)))


'''
分组：
概念： 除了简单的判断是否匹配外，正则表达式还有提取子串的功能，用（）表示提取分组
'''

str4 = '010-55321654'
m = re.match(r'((?P<first>\d{3})-(?P<last>\d{8}))',str4)
# 使用序号获取对应组的信息，group(0)代表原字符串
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group('first'))
# 查看匹配各组的情况
print(m.groups())