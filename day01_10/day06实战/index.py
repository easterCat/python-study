# 寻找水仙花数
def shui_xian_hua():
    for num in range(100, 1000):
        num1 = num % 10
        num2 = num // 10 % 10
        num3 = num // 100
        if num == num1 ** 3 + num2 ** 3 + num3 ** 3:
            print(num)


shui_xian_hua()


# 百钱百鸡问题

def get_total_chicken():
    for x in range(0, 20):
        for y in range(0, 33):
            z = 100 - x - y
            if 5 * x + 3 * y + z / 3 == 100:
                print('公鸡: %d只,母鸡: %d只,小鸡: %d只' % (x, y, z))


get_total_chicken()

from random import randint


# craps赌博游戏
def craps_game():
    money = 1000
    while money > 0:
        print('你的总资产:{}'.format(money))
        need_go_on = False
        while True:
            debt = int(input('请下注: '))
            if 0 < debt < money:
                break
        first = randint(1, 6) + randint(1, 6)
        if first == 7 or first == 11:
            print('玩家获胜!')
            money += debt
        elif first == 2 or first == 3 or first == 12:
            print('庄家获胜!')
            money -= debt
        else:
            need_go_on = True

        while need_go_on:
            need_go_on = False
            current = randint(1, 6) + randint(1, 6)
            print("玩家的点数: {}".format(current))
            if current == 7:
                print('庄家获胜!')
                money -= debt
            elif current == first:
                print('玩家获胜!')
                money += debt
            else:
                need_go_on = True
    print('破产')


craps_game()
