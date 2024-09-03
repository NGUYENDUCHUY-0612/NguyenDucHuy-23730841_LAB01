# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 10:30:00 2024

@author: Nguyễn Đức Huy - 23730841
"""

# Nhập ngày, tháng, năm từ người dùng
ngay = int(input("Nhập ngày sinh: "))
thang = int(input("Nhập tháng sinh: "))
nam = int(input("Nhập năm sinh: "))

# a) Ngày/tháng/năm
print(f"Định dạng ngày/tháng/năm: {ngay}/{thang}/{nam}")

# b) Ngày/tháng/năm (2 chữ số cuối của năm)
print(f"Định dạng ngày/tháng/năm (2 chữ số cuối): {ngay}/{thang}/{str(nam)[-2:]}")

# c) Năm/tháng/ngày
print(f"Định dạng năm/tháng/ngày: {nam}/{thang}/{ngay}")
