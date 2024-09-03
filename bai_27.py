# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 16:47:17 2024

@author: Nguyễn Đức Huy - 23730841
"""

import math
loại_hình = input("Nhập hình (v cho hình vuông, n cho hình chữ nhật, t cho hình tròn): ")
if loại_hình == 'v':
    a = float(input("Nhập chiều dài cạnh của hình vuông: "))
    p = 4 * a
    s = a * a
    print("Chu vi =",p)
    print("Diện tích =",s)
elif loại_hình == 'n':
    b = float(input("Nhập chiều rộng của hình chữ nhật: "))
    a = float(input("Nhập chiều dài của hình chữ nhật: "))
    p = 2 * (a + b)
    s = a * b
    print("Chu vi =",p)
    print("Diện tích =",s)
elif loại_hình == 't':
    r = float(input("Nhập bán kính của hình tròn: "))
    p = 2 * math.pi * r
    s = math.pi * (r ** 2)
    print("Chu vi =",p)
    print("Diện tích =",s)
else:
    print("Không tìm thấy hình.")