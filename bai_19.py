# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 11:15:38 2024

@author: Nguyễn Đức Huy - 23730841
"""

a=int(input("Số nguyên a: "))
b=int(input("Số nguyên b: "))
c=int(input("Số nguyên c: "))
d=int(input("Số nguyên d: "))
if (a<b and a<c and a<d) or (a==b and a<c and a<d) or (a==c and a<b and a<d) or (a==d and a<b and a<c):
    print("Số có giá trị nhỏ nhất là:",a)
elif (b<a and b<c and b<d) or (a==b and b<c and b<d) or (b==c and b<a and b<d) or (b==d and b<a and b<c):
    print("Số có giá trị nhỏ nhất là:",b)
elif (c<b and c<a and c<d) or (c==b and c<a and c<d) or (a==c and c<b and c<d) or (c==d and c<b and c<a):
    print("Số có giá trị nhỏ nhất là:",c)
else:
    print("Số có giá trị nhỏ nhất là:",d)