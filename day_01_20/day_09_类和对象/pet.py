from abc import abstractmethod, ABCMeta


class Pet(object, metaclass=ABCMeta):
    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        pass


class Dog(Pet):
    def make_voice(self):
        print('汪汪汪')


class Cat(Pet):
    def make_voice(self):
        print('miaomiaomiao')


def main():
    # test_pet = Pet('test')
    # test_pet.make_voice()
    """多态"""
    pets = [Dog('gou'), Cat('carry'), Dog('pig')]
    for pet in pets:
        pet.make_voice()


if __name__ == '__main__':
    main()
