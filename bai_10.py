# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 09:56:36 2024

@author: Nguyễn Đức Huy - 23730841
"""

so_xe = input("Nhập số xe của bạn (gồm 4 chữ số): ")

if len(so_xe) == 4 and so_xe.isdigit():
    tong_nut = sum(int(chu_so) for chu_so in so_xe)
    print(f"Tổng các chữ số (số nút) của số xe {so_xe} là: {tong_nut}")
else:
    print("Vui lòng nhập đúng số xe gồm 4 chữ số.")