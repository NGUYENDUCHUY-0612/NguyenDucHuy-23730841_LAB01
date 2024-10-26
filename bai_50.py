# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 11:01:59 2024

@author: Nguyễn Đức Huy - 23730841
"""
#Bài 50
def ktra_so(n):
    if n < 0 and n%2 !=0:
        return -1
    elif n>0 and n%2 == 0:
        return 1 
    return 0 
if __name__=='__main__':
    print(ktra_so(6))