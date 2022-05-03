# n 이 입력되면 k를 빼서 제곱수를 만들 수 있는 k를 구하고,
#
# 그 제곱수에 루트를 씌운 수(제곱근) t를 구하여라.
#
# 이 때 k는 여러가지가 될 수 있는데 가장 작은 k를 출력한다.

import math
a = int(input())
b = 0
"""
for i in range(a, 0, -1):
    if i * i < a:
        b = a - (i * i)
        print(b, i)
        break
"""
for i in range(1, a):
    if math.sqrt(a - i) % 1 == 0:
        b = i
        a = int(math.sqrt(a - 1))
        break
print(b, a)
