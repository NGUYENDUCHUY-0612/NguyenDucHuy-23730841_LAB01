# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 09:37:48 2024

@author: Nguyễn Đức Huy - 23730841
"""

import math
def Tinhchuvivadientichhinhtron():
    Bankinh = float(input("Nhập bán kính đường tròn = "))
    Chuvi = 2 * math.pi * Bankinh
    Dientich = math.pi * Bankinh ** Bankinh
    print("Chu vi hình tròn là :", Chuvi)
    print("Diện tích hình tròn là :", Dientich)
Tinhchuvivadientichhinhtron()