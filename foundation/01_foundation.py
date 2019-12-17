"""
@Author: matt
@Date : 2019/11/19
@Desc : python基础
"""
import random


# 变量
# 变量类型：整形、浮点型、字符串型、布尔型、复数型(了解 3+5j)
# 变量命名：
# 硬性：
# 1、变量命名由字母、下划线、数字构成，数字不能开头
# 2、大小写敏感
# 3、不要跟关键字以及系统保留字重合
# 规范：
# 1、用小写字母拼写，多个单词用下划线隔开
# 2、受保护的实例属性用单个下划线开头
# 3、私有的实例属性用双个下划线开头


def variable():
    a = 100
    b = 12.314
    c = 1 + 5j
    d = True
    e = "hello world"
    print(type(a))  # <class 'int'>
    print(type(b))  # <class 'float'>
    print(type(c))  # <class 'complex'>
    print(type(d))  # <class 'bool'>
    print(type(e))  # <class 'str'>


# 运算
# + - * / % //(取下整) **(幂)
def calc():
    a = int(input("a = "))
    b = int(input("b = "))
    print('%d + %d = %d' % (a, b, a + b))
    print('%d - %d = %d' % (a, b, a - b))
    print('%d * %d = %d' % (a, b, a * b))
    print('%d / %d = %d' % (a, b, a / b))
    print('%d // %d = %d' % (a, b, a // b))
    print('%d %% %d = %d' % (a, b, a % b))
    print('%d ** %d = %d' % (a, b, a ** b))


# if else 分支结构
def switch():
    admin = input("请输入用户名：")
    password = input("请输入密码：")
    if admin == "user" and password == "123456":
        print("身份认证成功")
    else:
        print("身份认证失败")


# for-in 循环结构
# range(101)可以产生一个0到100的整数序列
# range(1, 100)可以产生一个1到99的整数序列
# range(1, 100, 2)可以产生一个1到99的奇数序列，其中2是步长，即数值序列的增量
def get_sum():
    temp = 0
    for i in range(101):
        temp += i
    print(temp)


# while 循环
def guess_num():
    answer = random.randint(1, 100)
    counter = 0
    while True:
        counter += 1
        _guess_num = int(input("请输入猜测数字"))
        if _guess_num > answer:
            print("大一点")
        elif _guess_num < answer:
            print("小一点")
        else:
            print("猜对了")
            break
    print('你总共猜了%d次' % counter)
    if counter > 7:
        print('你的智商余额明显不足')


# 嵌套循环
def multiplication_table():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print("%d * %d = %d" % (i, j, i * j), end='\t')
        print()


# 函数 默认参数 print(roll_dice(m=4,n=5)) 调用时可以指定nm的值 不按照顺序
def roll_dice(n=2, m=3):
    total = 0
    print(m)
    for _ in range(n):
        total += random.randint(1, 6)
    return total


# 模块相关
import module1 as m1
import module2 as m2


def module_test():
    m1.foo()
    m2.foo()



