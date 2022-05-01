"""
두 실수 a, b가 입력되면 그 두수를 더하거나 빼거나 곱하거나 나누거나 제곱을 해서 가장 큰 수를 출력하시오.

예를 들어 1과 2가 입력되면,

1+2 = 3   , 2+1 = 3

1 - 2 = -1,   2 - 1 = 1

1 * 2 = 2,    2 * 1 = 2

1 / 2 = 0.5,   2 / 1 = 2

12=1 ,   21 = 2

따라서 최댓값은 3이다.
"""
import math
a, b = input().split()
a = int(a)
b = int(b)
a1 = a + b
a2 = a - b
a7 = b + a
a8 = b - a
a3 = a * b
a4 = a / b
a5 = math.pow(a,b)
a6 = math.pow(b,a)
arr = [a1, a2, a3, a4, a5, a6, a7, a8]
fmax = float(arr[0])
for i in range(8):
    if fmax<arr[i]:
        fmax = arr[i]

print(format(fmax,".6f"))        
