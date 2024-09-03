# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 12:00:49 2024

@author: Nguyễn Đức Huy - 23730841
"""

import math
def Phuongtrinh():
    a = float(input("Nhập a = "))
    b = float(input("Nhập b = "))
    c = float(input("Nhập c = "))
    if a == 0:
        if b == 0:
            if c == 0:
                print("Phương trình có vô số nghiệm.")
            else:
                print("Phương trình vô nghiệm.")
        else:
            x = -c / b
            print("Phương trình bậc 1 có nghiệm duy nhất x =", x)
    else:
        Denta = b ** 2 - 4 * a * c  
        
        if Denta > 0:
            x1 = (-b + math.sqrt(Denta)) / (2*a)
            x2 = (-b - math.sqrt(Denta)) / (2*a)
            print(f"Phương trình có hai nghiệm phân biệt: x1 = {x1} và x2 = {x2}")
        elif Denta == 0:
            x = -b / (2*a)
            print(f"Phương trình có nghiệm kép: x = {x}")
        else:
            print("Phương trình vô nghiệm")
Phuongtrinh()