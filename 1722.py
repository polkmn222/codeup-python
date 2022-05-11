# n 개 점의 좌표(x,y)를 입력받아 각 점을 순서대로 연결한 총 거리를 구하는 프로그램을 작성하시오.
#
# 단 마지막 점과 첫 번째 점은 연결하지 않는다.

import math

num = int(input())

x = []
y = []
length = 0

for i in range(num):
    a, b = input().split()
    a = int(a)
    b = int(b)
    x.append(a)
    y.append(b)

# print(b)
# print(c)

for i in range(0, num-1):
    x[i] -= x[i+1]
    y[i] -= y[i+1]
    length += math.sqrt((x[i] * x[i]) + (y[i] * y[i]))
    # print(length)

print('%.2f' % length)