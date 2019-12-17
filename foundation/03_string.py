"""
@Author: matt
@Date : 2019/11/21
@Desc : 字符串相关
"""
import sys


def string_show():
    # 字符串表示方式：
    a = 'aaa',
    b = "bbb",
    c = """
    支持换行文本
    """
    print(a, b, c, end="")


def string_transfer():
    s1 = "\'hello world\'"
    s2 = "\t\'hello world\'\t\n"
    s3 = "\141"  # 8进制
    s4 = "\x61"  # 16进制
    s5 = "\1793"  # 十进制
    s6 = '\u5f6c\u6d9b'  # unicode编码 转中文
    s7 = r'\'hello, world!\''  # 不做转译
    s8 = r'\n\\hello, world!\\\n'  # 不做转译
    print(s1, s2, s3, s4, s5, s6, s7, s8, end="")


def string_operate():
    s1 = "hello " * 3  # 重复字符串内容
    s2 = s1 + "world"  # + 拼接
    exist = "ll" in s1  # 字符串是否包含另一个字符串
    not_exist = "ll" not in s1
    s3 = "abcdefghijklmn"
    s4 = s3[4]  # 取下标为4
    s5 = s3[2:5]  # 取2-5位
    s6 = s3[2:]  # 从2位起
    s7 = s3[2::2]  # 从2位起，跨度2
    s8 = s3[::2]  # 从0位起，跨度2
    s9 = s3[::-1]  # 倒序
    s10 = s3[-3:-1]  # 从倒数第三位 取倒数第一位

    print(s1, s2, exist, not_exist)
    print(s4, s5, s6, s7, s8, s9, s10)


def string_operate2():
    s1 = "hello,world"
    length = len(s1)
    s2 = s1.capitalize()
    s3 = s1.title()
    s4 = s1.upper()
    s5 = s1.find("hello")
    s6 = s1.index("or")
    # s6 = s1.index("java")
    s7 = s1.startswith("He")
    s8 = s1.endswith("me")
    s9 = s1.center(50, '*')
    s10 = s1.rjust(10, "*")
    s11 = s1.isalnum()
    s12 = s1.isalpha()
    s13 = s1.isdigit()
    print(length, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13)


def list_show():
    list1 = [0, 3, 5, 7, 110, "222"]
    list2 = ["hello"] * 3
    length = len(list1)
    for index in range(len(list1)):
        print(list1[index])
    for elem in list1:
        print(elem)
    for index, elem in enumerate(list1):
        print(f"{index}:{elem}")
    print(f"list1:{list1},list2:{list2},length:{length}")


def list_operate():
    list1 = [0, 3, 5, 7, 110, "222"]
    list1.insert(1, 23)  # 插入位数 指定位置
    list1.append(50)  # 添加元素
    list1.extend([1000, 5000])  # 列表合并1
    list1 += [3000, 2000]  # 列表合并2
    exist = 3000 in list1
    if 3000 in list1:
        list1.remove(3000)  # 值删除
    print(f"list1:{list1},exist:{exist}")
    list1.pop(2)  # 指定位置删除
    print(f"list1:{list1}")
    list1.clear()  # 列表清除


def list_operate2():
    fruits = ['grape', 'apple', 'strawberry', 'orange']
    fruits += ['banana', 'pear', 'mango']
    fruits2 = fruits[1:4]  # 列表切片
    fruits6 = fruits[-3: -1]  # 列表切片
    fruits3 = fruits[:]  # 列表复制
    fruits4 = fruits[::-1]  # 反向复制
    print(f"fruits2:{fruits2},fruits3:{fruits3},fruits4:{fruits4},fruits6:{fruits6}")


def list_sort():
    list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    list2 = sorted(list1)
    list3 = sorted(list1, reverse=True)  # 倒序
    list4 = sorted(list1, key=len)
    print(f"list2:{list2},list3:{list3},list4:{list4}")
    list1.sort(reverse=True)
    print(f"list1:{list1}")


def list_gen():
    # 用列表的生成表达式语法创建列表容器
    # 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
    list1 = [x for x in range(1, 10)]
    list2 = [x + y for x in "ABCDEFGHIJKLMN" for y in "123456789"]
    print(f"list:{list1},list2:{list2}")
    # 查看占用内存
    print(sys.getsizeof(list2))  # 表达式创建的是一个列表，会占用较多的内存空间
    # 生成器 相当于占位符
    f = (x ** 2 for x in range(1, 30))
    print(sys.getsizeof(f))
    print(f)
    for element in f:
        print(element)


def fib(n):
    # yield 生成器
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a  # yield关键字将一个普通函数改造成生成器函数


def tuple_show():
    t = ("马彬涛", "广东汕头", 23, "篮球")
    print(t)
    print(t[0], t[1])  # 下标取值
    for item in t:
        print(item)  # 遍历取值
    # t[0] = "Matt"  TypeError: 'tuple' object does not support item assignment(元祖数据不支持修改)
    person = list(t)  # 转列表
    person[0] = "Matt"  # 列表支持重新赋值
    t = tuple(person)  # 列表转元祖 间接更改元祖数据

    print(t)

    # 元祖与列表：
    # 1、元祖数据不可变，不变的对象更易于维护，线程安全，无需考虑线程同步
    # 2、元祖效率高于列表


def set_show():
    # 集合创建
    set1 = {1, 2, 3, 4, 5, 6}
    print(set1, len(set1))
    set2 = set(range(1, 10))
    set3 = set((1, 2, 3, 3, 2, 1))
    print(set2, set3)
    # 创建集合的推导式语法(推导式也可以用于推导集合)
    set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
    print(set4)

    # 集合元素操作
    set1.add(7)  # 添加单个
    set2.update([10, 11])  # 添加多个
    set2.discard(10)  # 值删除
    if 4 in set2:
        set2.remove(4)
    set2.pop()  # 删除首位
    print(set2)

    # 集合运算
    print(f"set1:{set1},set2:{set2}")
    print(f"intersection:{set1 & set2}")
    print(f"union:{set1 | set2}")
    print(f"difference:{set1 - set2}")  # 返回A中存在 B中不存在的数据
    print(f"symmetric_difference{set1 ^ set2}")  # 返回两个集合中不重复的数据

    # 判断字集或超集
    print(set2 <= set1)
    print(set2 >= set1)


def dict_show():
    # 字典创建
    dict1 = {'name': 'Matt', 'age': '23', 'hobby': 'code'}  # 方式一
    dict2 = dict(name="马彬涛", age="23", hobby="code")  # 方式二
    dict3 = dict(zip(['name', 'age', 'hobby'], ['Ljx', '23', 'write']))  # 方式三：通过zip函数将两个序列压成字典
    dict4 = {num: num ** 2 for num in range(1, 10) if num < 3}  # 方式四：创建字典的推导式语法
    print(f"dict1:{dict1},dict2:{dict2},dict3:{dict3},dict4:{dict4}")

    # 字典取值
    print(dict1['name'])
    for key in dict1:
        print(f"key:{key},value:{dict1[key]}")
    print(dict1.get("height", 168))  # 取不到 使用默认值

    # 字典修改
    dict1['name'] = '马彬涛'
    dict2.update(name="Ljx", age="22", height=168)  # 存在修改 不存在新增
    dict3.popitem()  # 返回 推出的元素 kv形式
    dict4.pop(1, 10)  # 第一个值表示key值，第二个值表示获取不到时的默认值，如果没有默认值，key值必须存在，返回key对应的value
    print(dict1, dict2, dict3, dict4)

    # 字典七个纽扣给你


if __name__ == '__main__':
    # string_show()
    # string_transfer()
    # string_operate()
    # string_operate2()
    # list_show()
    # list_operate()
    # list_operate2()
    # list_sort()
    # list_gen()

    # for val in fib(20):
    #     print(val)

    # tuple_show()
    # set_show()
    dict_show()
