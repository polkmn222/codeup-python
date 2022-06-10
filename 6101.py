# 1. numpy 패키지를 np라는 이름으로 불러오기
# 2. 첫째 줄에 numpy 버전 출력하기
# 3. 사이즈가 10인 넘파이 배열에 0을 채워서 출력하기 - zeros 이용
# 4. 위 배열을 5번째 원소만 1로 변경해서 출력하기


import numpy as np

print(np.__version__)
zero_array = np.zeros(10)
print(zero_array)
# print(type(zero_array))
zero_array[4] = 1
value = zero_array[4]
print(zero_array)