# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 16:30:39 2024

@author: Nguyễn Đức Huy - 23730841
"""

#a
print ("a.")
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
print("Thứ tự tăng dần: ", a, b, c)
#b
print("b.")
N = input("Nhập số nguyên: ")
dayso = "".join(sorted(N))
print("Dãy số theo thứ tự tăng dần: ", dayso)