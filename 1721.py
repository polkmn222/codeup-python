# 두 점의 좌표(x,y)를 입력받아 두 점 간의 거리를 구하는 프로그램을 작성하시오.

import math

x1, y1 = input().split()
x2, y2 = input().split()

x1 = int(x1)
x2 = int(x2)
y1 = int(y1)
y2 = int(y2)

a = math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))

print('%.2f' % a)