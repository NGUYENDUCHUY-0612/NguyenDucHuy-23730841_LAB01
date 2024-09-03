# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 10:20:00 2024

@author: Nguyễn Đức Huy - 23730841
"""

import random
#a> 0 đến 100:
a = random.randint(0,100)
b = random.uniform(0,100)
print ("Một số nguyên ngẫu nhiên từ 0 đến 100: ", a)
print ("Một số thực ngẫu nhiên từ 0 đến 100: ", b)

#b> 50 đến 90:
c = random.randint(50,90)
d = random.uniform(50,90)
print ("Một số nguyên ngẫu nhiên từ 50 đến 90: ", c)
print ("Một số thực ngẫu nhiên từ 50 đến 90: ", d)

#c> -39 đến 79:
x = random.randint(-39,79)
y = random.uniform(-39,79)
print ("Một số nguyên ngẫu nhiên từ -39 đến 79: ", x)
print ("Một số thực ngẫu nhiên từ -39 đến 79: ", y)

#d> -79 đến -39:
z = random.randint(-79,-39)
t = random.uniform(-79,-39)
print ("Một số nguyên ngẫu nhiên từ -79 đến -39: ", z)
print ("Một số thực ngẫu nhiên từ -79 đến -39: ", t)
