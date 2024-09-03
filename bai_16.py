# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 10:47:26 2024

@author: Nguyễn Đức Huy - 23730841
"""

a = int(input("Nhập giờ: "))
b = int(input("Nhập phút: "))
c = int(input("Nhập giây: "))
d = a*3600+b*60+c
print("Thời gian",f"{a}h{b}p{c}s","=",d,"giây")