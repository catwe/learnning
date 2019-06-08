
import re
'''
判断字符串是否为电话号码
'''

def checkPhone(str):
    if len(str)!=11:
        return False
    elif str[0]!='1':
        return False
    elif str[1:3]!='85'and str[1:3]!='39':
        return False
    for i in range(3,11):
        if str[i]<'0' or str[i]>'9':
            return False
    return True


 # 18581386296
def checkPhone1(str):
    pat = r"(1(([3578]\d)|(47))\d{8}$)"
    res = re.findall(pat, str)
    print(res)




print(checkPhone('18581386296'))
checkPhone1('sasf18512345678')