# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 11:10:04 2024

@author: Nguyễn Đức Huy - 23730841
"""
#Bài 54
def fibonacci(n):
  """In n số Fibonacci đầu tiên.

  Args:
    n: Số lượng số Fibonacci cần in.
  """

  a, b = 0, 1
  while a < n:
      print(a, end=' ')
      a, b = b, a+b
      
  
print(fibonacci(2024))