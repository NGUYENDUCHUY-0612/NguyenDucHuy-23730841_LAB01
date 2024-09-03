# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 09:45:14 2024

@author: Nguyễn Đức Huy - 23730841
"""


def TinhBMI():
    Cannang = float(input("Nhập cân nặng của bạn'kg' = "))
    Chieucao = float(input("Nhập chiều cao của bạn'm' = "))
    BMI = Cannang / (Chieucao ** 2)
    BMI = round(BMI, 2)
    print("Chỉ số BMI của bạn là : ", BMI)
TinhBMI()