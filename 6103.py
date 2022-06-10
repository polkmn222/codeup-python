# 1. 넘파이 랜덤 씨드 값을 32로 초기화한다. - random.seed
# 2. random 함수를 이용하여 3x3x3 배열을 만들어 출력한다. - random.random
# 3. random 함수를 이용하여 10x10 배열을 만들고, 최솟값 최댓값을 한 줄에 출력한다. - min max
# 4. random함수를 이용하여 30개의 원소를 만들고 평균 값을 출력한다. - mean

import numpy as np

np.random.seed(32)
print(np.random.random((3, 3, 3)))

a = np.random.rand(10, 10)
print(np.min(a), np.max(a))

a = np.random.rand(30)
print(np.mean(a))