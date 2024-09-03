# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 11:50:44 2024

@author: Nguyễn Đức Huy - 23730841
"""

a = float (input("a = "))
b = float (input("b = "))

print ("Giải phương trình bậc nhất: ax + b = 0")
if a==0:
    if b==0:
        print ("Phương trình bậc nhât có vô số nghiệm.")
    else:
        print ("Phương trình bậc nhất vô nghiệm.")
else:
    print ("Phương trình bậc nhất có 1 nghiệm duy nhất x = ",-b/a)