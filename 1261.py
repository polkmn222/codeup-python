"""
10개의 수가 입력 된다.

10개의 수 중 5의 배수를 하나만 출력 한다.

만약 5의 배수가 없다면 0을 출력 한다.
"""
num = list(map(int, input().split()))
b = 0
for i in range(len(num)):
    # print(num[i])
    b = num[i]
    if num[i] % 5 == 0:
        print(num[i])
        break
if b % 5 != 0:
    print(0)


