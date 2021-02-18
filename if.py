
import math
from random import randint  # 隨機整數值

face = randint(1, 6)  # 隨機1 ~ 6
if face == 1:
    result = '唱首歌'
elif face == 2:
    result = '跳個舞'
elif face == 3:
    result = '學狗叫'
elif face == 4:
    result = '做俯臥撑'
elif face == 5:
    result = '念繞口令'
else:
    result = '講冷笑話'
print(result)


a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    print('周長: %f ' % (a + b + c))
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print('面積: %f ' % (area))
else:
    print('不能構成三角形')
