"""
@Author: matt
@Date : 2019/11/20
@Desc : 习题
"""
from random import randint


def get_all_narcissistic_num():
    # 寻找水仙花数，是一个三位数，且数字每位上的数字立方之和等于它本身，例如：$1^3 + 5^3+ 3^3=153$
    for num in range(100, 1000):
        high = num // 100
        mid = num // 10 % 10
        low = num % 10
        if num == low ** 3 + mid ** 3 + high ** 3:
            print(num)


def reverse_num():
    # 正整数反转
    num = int(input("请输入正整数："))
    reverse = 0
    while num > 0:
        reverse = reverse * 10 + num % 10
        num //= 10
    print(reverse)


def craps():
    # craps 赌博游戏：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；玩家第一次如果摇出2点、3点或12点，庄家胜；其他点数玩家继续摇骰子。
    # 如果玩家摇出了7点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；其他点数，玩家继续要骰子，直到分出胜负。
    money = 1000;
    while money > 0:
        print("你的总资产为%d" % money)
        needs_go_on = False
        while True:
            debt = int(input("请输入赌注："))
            if 0 < debt <= money:
                break
            else:
                print("资产不足")
        first = randint(1, 6) + randint(1, 6)
        print("玩家第一次摇出%d点" % first)
        if first == 7 or first == 11:
            print("玩家胜")
            money += debt
        elif first == 2 or first == 3 or first == 12:
            print("庄家胜")
            money -= debt
        else:
            needs_go_on = True
        while needs_go_on:
            needs_go_on = False
            current = randint(1, 6) + randint(1, 6)
            print("玩家摇出%d点" % current)
            if current == first:
                print("玩家胜")
                money += debt
            elif current == 7:
                print("庄家胜")
                money -= debt
            else:
                needs_go_on = True
    print("你破产了")


craps()
