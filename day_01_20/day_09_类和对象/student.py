class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print("%s正在学习%s." % (self.name, course_name))

    def watch_movie(self):
        if self.age < 18:
            print('%s只能观看熊出没.' % self.name)
        else:
            print('%s可以观看恐怖片.' % self.name)


def main():
    stu1 = Student('刘德华', 55)
    stu1.study("歌词")
    stu1.watch_movie()
    stu2 = Student("成龙", 11)
    stu2.study('武打')
    stu2.watch_movie()


if __name__ == '__main__':
    main()
