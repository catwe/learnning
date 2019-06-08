import re

print('-------匹配单个字符与数字-----------')
'''
re 
.             匹配除换行符以外的任意字符
[0123456789]  []是字符集合，表示匹配方括号中所包含的任意一个字符
[wang]        匹配'w','a','n','g'中任意一个字符
[a-z]         匹配任意小写字母
[A-Z]         匹配任意大写字母
[0-9]         匹配任意数字，类似[0123456789] 
[0-9a-zA-Z]   匹配任意的数字和字母
[0-9a-zA-Z_]  匹配任意的数字、字母和下划线
[^wang]       匹配除了'wang'这几个字符以外的所有字符，中括号里的~称为脱字符，表示不匹配集合中的字符
[^0-9]        匹配到所有的非数字字符
\d            匹配数字，效果同[0-9]
\D            匹配到所有的非数字字符,效果同[^0-9]
\w            匹配任意的数字、字母和下划线,效果同[0-9a-zA-Z_]
\W            匹配任意的非数字字母和下划线,效果同[^0-9a-zA-Z_]
\s            匹配任意的空白符（空格，换行，回车，换页，制表），效果同[\f\n\r\t]
\S             匹配任意的非空白符（空格，换行，回车，换页，制表），效果同[^\f\n\r\t]

'''

print(re.search('[0123456789]','wangcong 8 is a good man 9'))
print(re.search('.','wangcong 8 is a good man 9'))
print(re.findall('\d','wangcong 8 is a good man 9'))
print(re.findall('[^0-9] ','wangcong 8 is a good man 9'))



print('--------------锚字符（边界字符）-----------')
'''
^         行首匹配，与[]中的不是一个意思
$         行尾匹配

\A        匹配字符串开始，它和^的区别是：\A只匹配整个字符串的开始，即使在re.M模式下也不会匹配他行的行首
\Z        匹配字符串结尾，它和$的区别是：\Z只匹配整个字符串的结尾，即使在re.M模式下也不会匹配他行的结尾

\b        匹配一个单词的边界，也就是指单词和空格间的位置,'er\b'可以匹配never,不可以匹配nerve
\B        匹配非单词边界


'''
print(re.search('man$','sunck is a good man'))

print(re.findall('^wang ','wang cong 8 is a good man 9 \nwang cong 8 is a good man',flags=re.M))
print(re.findall('\Awang ','wang cong 8 is a good man 9 \nwang cong 8 is a good man',flags=re.M))
print('*****************************')
print(re.findall('man$','wang cong 8 is a good man\nwang cong 8 is a good man',flags=re.M))
print(re.findall('man\Z','wang cong 8 is a good man\nwang cong 8 is a good man',flags=re.M))
print('*****************************')

print(re.search(r'er\b','never'))
print(re.search(r'er\b','nerve'))

print(re.search(r'er\B','never'))
print(re.search(r'er\B','nerve'))



print('---------------------匹配多个字符----------------')
'''
   说明：下方的x、y、z、n均为假设的普通字符，不是正则表达式的元字符（xyz）匹配小括号里的xyz（作为一个整体去匹配）
   x?  匹配0个或者1个x
   x*  匹配0个或者任意个x（.*表示匹配0个或者任意多个字符，换行符除外）
   x+  匹配至少一个x
   x{n} 匹配确定的n个x(n是一个非负整数)
   x{n,} 匹配至少n个x
   x{n,m} 匹配至少n个最多m个x,注意：n<=m
   x|y    表示或，匹配的是x或者y
'''
# 以上说明与以下代码一一对应
print(re.findall(r'(sunck)','sunckgood is a good man,sunck is a good man'))
print(re.findall(r'o?','oooosdasd'))#非贪婪匹配（尽可能少的匹配）
print(re.findall(r'a*','aaaapppsa'))#贪婪匹配（尽可能多的匹配）
print(re.findall(r'.*','aaaapppsa'))#贪婪匹配（尽可能多的匹配）
print(re.findall(r'a+','aaaapppsa'))#贪婪匹配（尽可能多的匹配）
print(re.findall(r'a{3}','aaapppsaa'))#匹配连续n个连在一起的a
print(re.findall(r'a{3,}','aaaapppsa'))#贪婪匹配（尽可能多的匹配）
print(re.findall(r'a{3,6}','aaaaaaaaapppsa'))#贪婪匹配（尽可能多的匹配）
print(re.findall(r'((s|S)unk)','sunk--Sunk---SunK'))



#需求，提取整个字符串sunck is a good man
str = 'sunck is a good man,sunck is a handson man,sunck is a nice man'
print(re.findall(r'^sunck.*man$',str))
print(re.findall(r'(^sunck.*?man$)',str))

print('--------------特殊----------------')
'''
+?  *?  x? 最小匹配，通常都是尽可能多的匹配，可以使用这种解贪婪匹配
'''

#注释：/* part1 */       /* part2 */
print(re.findall(r'(//*.*?/*/)',r'/* part1 */       /* part2 */'))#两个都匹配到了
print(re.findall(r'(//*.*/*/)',r'/* part1 */       /* part2 */'))#只匹配到一个字符串


