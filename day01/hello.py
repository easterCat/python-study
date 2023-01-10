#!/usr/bin/env python3
from ast import Name


print("hello world")
age = 20
if age >= 18:
    print("you age is", age)
else:
    print("kid")


birth = 22222
if birth < 2000:
    print("00前")
else:
    print("00后")

names = ["aaa", "bbb", "ccc"]
for name in names:
    print(name)

name = input("please input your name : ")
print("your name is", name)


a = input()
b = input()
print("a * b = ", str(int(a) * int(b)))
