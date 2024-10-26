# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 11:03:44 2024

@author: ADM
"""
#Bài 51
def  ktra_gtri():
    n = input("nhap n:")
    if n.replace('.','',1).replace('-','',1).isdigit():
        n = float(n)
#   if n.lstrip('-').isdigit():(-)123
    #   n = int(n)
#   if n.strip('-').isdigit():(-)123
    #   n = int(n)
    if -89 <= n <= 90:
        return n 
    print("ko hợp lệ, nhập lại:")
    return ktra_gtri()
if __name__=='__main__':
    print(ktra_gtri())
    