# -*- coding: utf-8 -*-

import math   # 使用 math 套件能直接使用圓周率
c = float(input('請輸入攝氏溫度: '))
f = c * 1.8 + 32
print(' %.1f  攝氏度 = %.1f  華氏度 ' % (c, f))


radius = float(input('請輸入圓的半徑: '))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('周長: %.2f ' % perimeter)
print('面積: %.2f ' % area)
