# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 11:06:47 2024

@author: Nguyễn Đức Huy - 23730841
"""
#Bài 52 
#a
def canbac(x,n):
    return x**(1/n)
#b
def sodao(n):
    #str: chuỗi, chữ số
    return str(n)[::-1]
    #return int(str(n)[::-1])
#Cách 3: tính toán
def dao(n):
   dao=0
   while n>0:
        dao=dao*10+n%10
        n//=10
   return dao
#c
def chinhphuong(n):
    import math
    return int(math.sqrt(n))**2 == n 
#d
def ktra_ngto(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True 
#e
def tich_sole(n):
    tich = 1
    for i in str(n):
        if int(i)%2 !=0:
            tich *= int(i)
    return tich
#f

def tong_ngto(n):
    tong_ngto = 0
    for i in range(2,n):
        if ktra_ngto(i):
            tong_ngto += i
    return tong_ngto
#g
def tong_chinhphuong(n):
    tong_chinhphuong=0
    for i in range(1,n):
        if chinhphuong(i):
            tong_chinhphuong += i 
    return tong_chinhphuong
#h
def tong_uoc(n):
    tong = 0
    for i in range(1,n+1):
        if n%i == 0:
            tong +=i
    return tong

if __name__ =='__main__':
    
    print(canbac(8,3))
    print(sodao(123450))
    print(dao(123450))
    print(chinhphuong(1))
    print(ktra_ngto(1))
    print(tich_sole(195))
    print(tong_ngto(20))
    print(tong_chinhphuong(9))
    print(tong_uoc(8))