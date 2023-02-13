from time import sleep, time, localtime


class Clock(object):
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    @classmethod
    def now(cls):
        c = localtime(time())
        return cls(c.tm_hour, c.tm_min, c.tm_sec)

    def run(self):
        self.s += 1
        if self.s == 60:
            self.s = 0
            self.m += 1
            if self.m == 60:
                self.m = 0
                self.h += 1
                if self.h == 24:
                    self.h = 0

    def show(self):
        print('%2d - %2d - %2d' % (self.h, self.m, self.s))


def main():
    clock = Clock(23, 59, 55)
    clock2 = Clock.now()
    while True:
        clock.show()
        clock2.show()
        sleep(1)
        clock.run()
        clock2.run()


main()
