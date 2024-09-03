# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 09:33:09 2024

@author: Nguyễn Đức Huy - 23730841
"""

thoi_gian = input("Nhập thời gian (định dạng hh:mm:ss): ")

gio, phut, giay = map(int, thoi_gian.split(':'))

tong_giay = gio * 3600 + phut * 60 + giay

print(f"Tổng số giây của {gio:02d}:{phut:02d}:{giay:02d} là: {tong_giay} giây")
