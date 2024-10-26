# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 11:11:28 2024

@author: Nguyễn Đức Huy - 23730841
"""
#Bài 55
def calculate_perimeter(length, width):
  """Tính chu vi hình chữ nhật.

  Args:
    length: Chiều dài.
    width: Chiều rộng.

  Returns:
    Chu vi hình chữ nhật.
  """

  return 2 * (length + width)

def calculate_area(length, width):
  """Tính diện tích hình chữ nhật.

  Args:
    length: Chiều dài.
    width: Chiều rộng.

  Returns:
    Diện tích hình chữ nhật.
  """

  return length * width

def draw_rectangle(length, width):
  """Vẽ hình chữ nhật bằng dấu *.

  Args:
    length: Chiều dài.
    width: Chiều rộng.
  """

  for _ in range(width):
    print("*" * length)

# Ví dụ sử dụng hàm
length = int(input("Nhập chiều dài: "))
width = int(input("Nhập chiều rộng: "))

perimeter = calculate_perimeter(length, width)
area = calculate_area(length, width)
print("Chu vi:", perimeter)
print("Diện tích:", area)
draw_rectangle(length, width)