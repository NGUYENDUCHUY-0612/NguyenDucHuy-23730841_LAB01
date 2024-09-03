# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 11:45:20 2024

@author: Nguyễn Đức Huy -23730841
"""

a=int(input("Nhập 1 số bất kì: "))
x= {0:"Khong",1:"Mot",2:"Hai",3:"Ba",4:"Bon",5:"Nam",6:"Sau",7:"Bay",8:"Tam",9:"Chin"}
if 0<=a<=9:
    print("Số vừa nhập là: ",x[a])
else:
    print("Khong doc duoc.")
 