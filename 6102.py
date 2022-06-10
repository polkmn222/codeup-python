# 1. 10, 11, 12, ..., 48, 49 원소를 갖는 넘파일 배열을 출력하시오.
# 2. 위 배열을 역순 배열로 만들어 출력하시오.
# 3. 0~8의 원소를 갖는 3x3 행렬을 만들어 출력하시오. - reshape 활용
# 4. [1,2,0,0,4,0]에서 0이 아닌 원소의 위치를 출력하시오. - nonzero 활용
# 5. 3x3의 단위 행렬을 만들어서 출력하시오. - eye 활용

import numpy as np

sq_array = np.arange(10, 50)
print(sq_array)
# print(sq_array.reverse())
# sq_array1 = sq_array.tolist()
# print(type(sq_array1))
# print(sq_array1)
# print(sq_array1)
# for i in reversed(sq_array1):
#     print(i, end=" ")
# print(list(reversed(sq_array)))

print(sq_array[::-1])
# sq_array2d = np.array(0, 8)
# sq_array2d = sq_array2d.reshape(3, 3)
# print(sq_array2d)

sq_array1 = np.arange(0, 9).reshape(3, 3)
print(sq_array1)

l1 = [1, 2, 0, 0, 4, 0]
array1 = np.array(l1)
print(np.nonzero(array1))

d = np.identity(3)
print(d)
# E1 = np.eye(3, dtype=int)
# print(E1)

