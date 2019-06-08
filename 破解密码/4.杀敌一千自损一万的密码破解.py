import itertools
import time
# repeat = 密码位数
# mylist = list(itertools.product('0123456789',repeat=1))
passwd = (''.join(x) for x in itertools.product('0123456789QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm!@#$%^&*()_+?/',repeat=6) )
# print(mylist)
# print(len(mylist))

while True:
    try:
        time.sleep(0.5)
        str = next(passwd)
        print(str)
    # 到零之后会报错，采用以下代码解决此问题
    except StopIteration as e:
        break

