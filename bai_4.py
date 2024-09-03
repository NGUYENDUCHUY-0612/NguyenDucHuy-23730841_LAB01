# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 09:25:06 2024

@author: Nguyễn Đức Huy - 23730841
"""

N = float(input("Nhập giá trị N: "))
a = N//10
b = N%10
if N > 9 and N < 99:
    print("Tổng 2 số là: ", a+b)
else:
    print("Số của bạn nhập không hợp lệ")