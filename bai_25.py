# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 16:06:41 2024

@author: 
"""

a = input("Hãy nhập một chữ cái: ")
if a.islower():
    print("Ký tự chữ hoa:", a.upper())
else:
    print("Ký tự chữ thường:", a.lower())