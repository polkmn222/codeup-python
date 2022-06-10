# 1. 10x10의 2차원 배열의 테두리는 1이고 안은 0인 배열을 출력하시오.
# 2. 8x8의 2차원 배열에 아래와 같은 체크 보드를 만들어 출력하시오.(주의:정수타입)

import numpy as np

one = np.zeros((10, 10))

# print(one)
for i in range(0, 10):
    one[0][i] = 1
    one[9][i] = 1
    one[i][0] = 1
    one[i][9] = 1

print(one)

two = np.zeros((8, 8), dtype='int32')

for i in range(0, 8):
    if i == 0 or i % 2 == 0:
        two[1][i] = 1
        two[3][i] = 1
        two[5][i] = 1
        two[7][i] = 1
    elif i == 0 or i % 2 != 0:
        two[0][i] = 1
        two[2][i] = 1
        two[4][i] = 1
        two[6][i] = 1

print(two)