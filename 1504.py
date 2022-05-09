# 하나의 정수 N을 입력받아 다음과 같이 지그재그로 출력하시오.

a = int(input())
b = [[0]*a for i in range(a)]
c = 0

for i in range(a):
    if i % 2 == 0:
        for j in range(a):
            c += 1
            b[j][i] = c
    else:
        for j in range(a-1, -1, -1):
            c += 1
            b[j][i] = c

for i in range(a):
    for j in range(a):
        print(b[i][j], end=" ")
    print()