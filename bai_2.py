# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 08:59:18 2024

@author: Nguyễn Đức Huy - 23730841
"""


a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

tong = a + b
hieu = a - b
tich = a * b

if b != 0:
    thuong_2_chu_so = round(a / b, 2)
    thuong_3_chu_so = round(a / b, 3)
else:
    thuong_2_chu_so = "Không xác định (chia cho 0)"
    thuong_3_chu_so = "Không xác định (chia cho 0)"

print(f"Tổng của {a} và {b} là: {tong}")
print(f"Hiệu của {a} và {b} là: {hieu}")
print(f"Tích của {a} và {b} là: {tich}")
print(f"Thương của {a} và {b} làm tròn 2 chữ số là: {thuong_2_chu_so}")
print(f"Thương của {a} và {b} làm tròn 3 chữ số là: {thuong_3_chu_so}")
