"""
초를 입력받아 분 / 초의 형태로 출력하시오.

예)

60  ====>   1 0    (1분 0초를 뜻함)

70    ====>    1  10       (1분 10초를 뜻함)
"""
import math
a = int(input())
b = math.floor(a / 60)
c = a % 60

print(b, c)
