# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 11:09:26 2024

@author: Nguyễn Đức Huy - 23730841
"""
#Bài 53
def tong_1(n):
    s =0
    for i in range(1,n+1):
        s += i 
    return  s

def tong_2(n):
    s = 0
    for i in range(1,n+1):
        s +=i**2
    return s

def tong_3(n):
    s = 0
    for i in range(1,n+1):
        s +=1/i
    return s

def tong_4(n):
    s = 0
    giaithua = 1 
    for i in range(1,n+1):
        giaithua *=i
        s += giaithua
    return s 

def tong_5(n):
    giaithua = 1 
    for i in range(1,n+1):
        giaithua *=i
    return giaithua

if __name__ =="__main__":
    print(tong_1(5))
    print(tong_2(4))
    print(tong_3(4))
    print(tong_4(5))
    print(tong_5(5))