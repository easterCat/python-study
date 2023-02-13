import random
from abc import abstractmethod
from random import randint


class Fighter(object):
    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        pass


class Ultraman(Fighter):
    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        other.hp -= randint(15, 25)
        print('奥特曼{}对小怪兽{}发动了普通攻击'.format(self._name, other.name))

    def huge_attack(self, other):
        if self._mp >= 50:
            self._mp -= 50
            other.hp -= randint(50, 75)
            print('奥特曼{}对小怪兽{}发动了必杀技'.format(self._name, other.name))
        else:
            print('MP不够,奥特曼{}对小怪兽{}发动了普通攻击'.format(self._name, other.name))
            self.attack(other)
            return False

    def magic_attack(self, other):
        if self._mp > 20:
            self._mp -= 20
            other.hp -= randint(25, 35)
            print('奥特曼{}对小怪兽{}发动了魔法攻击'.format(self._name, other.name))
        else:
            print('MP不够,奥特曼{}对小怪兽{}发动了普通攻击'.format(self._name, other.name))
            self.attack(other)
            return False

    def resume(self):
        if self._mp <= 100:
            self._mp += randint(20, 30)
        else:
            self._mp += randint(15, 20)

    def __str__(self):
        return '奥特曼{}当前: '.format(self._name) + 'HP: %d' % self._hp + ', ' + 'MP: %d' % self._mp


class Monster(Fighter):
    __slots__ = ('_name', '_hp')

    def attack(self, other):
        other.hp -= randint(15, 25)
        print('小怪兽{}对奥特曼{}发动了普通攻击'.format(self._name, other.name))

    def __str__(self):
        return '小怪兽{}当前: '.format(self._name) + 'HP: %d' % self._hp


def is_any_alive(monsters):
    for monster in monsters:
        if monster.alive > 0:
            return True
    return False


def select_one_alive_monster(monsters):
    m_len = len(monsters)
    while True:
        index = random.randrange(m_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster


def display_info(atm, monsters):
    print("**********当前战斗状态**********")
    print(atm)
    for monster in monsters:
        print(monster, end=', ')


def main():
    atm = Ultraman("amd7900", 1000, 130)
    m1 = Monster("rtx1060", 300)
    m2 = Monster("rtx2070", 500)
    m3 = Monster("rtx3080", 700)
    ms = [m1, m2, m3]
    fight_round = 1
    while atm.alive and is_any_alive(ms):
        print("当前第%d回合" % fight_round)
        m = select_one_alive_monster(ms)
        skill = randint(1, 10)
        if skill <= 6:
            atm.attack(m)
            atm.resume()
        elif skill <= 9:
            atm.magic_attack(m)
            atm.resume()
        else:
            atm.huge_attack(m)
            atm.resume()
        if m.alive > 0:
            m.attack(atm)
        display_info(atm, ms)
        fight_round += 1
    print('战斗结束')
    if atm.alive > 0:
        print('奥特曼{}胜利'.format(atm.name))
    else:
        print('小怪兽胜利')


if __name__ == '__main__':
    main()
