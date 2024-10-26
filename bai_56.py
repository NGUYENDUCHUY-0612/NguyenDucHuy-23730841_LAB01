# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 08:27:28 2024

@author: Nguyễn Đức Huy - 23730841
"""
#Bài 56 
import math

def tinh(a, b=None, hinh='vuong', tinh='cv'):
  """
  Hàm tính chu vi hoặc diện tích của hình học đơn giản.

  Args:
    a: Số đo cạnh, bán kính hoặc chiều dài.
    b: Chiều rộng (chỉ dùng cho hình chữ nhật).
    hinh: Loại hình (vuông, tròn, chữ_nhật).
    tinh: Tính toán (cv: chu vi, dt: diện tích).
  """

  if hinh == 'vuong':
    if tinh == 'cv':
      return 4 * a
    elif tinh == 'dt':
      return a * a
  elif hinh == 'tron':
    if tinh == 'cv':
      return 2 * math.pi * a
    elif tinh == 'dt':
      return math.pi * a * a
  elif hinh == 'chu_nhat':
    if tinh == 'cv':
      return 2 * (a + b)
    elif tinh == 'dt':
      return a * b
  else:
    return "Hình không hợp lệ"


print(tinh(10, hinh='vuong', tinh='cv'))
print(tinh(50, hinh='vuong', tinh='dt'))
print(tinh(18, hinh='tron', tinh='cv'))
print(tinh(20, 30, hinh='chu_nhat', tinh='cv'))