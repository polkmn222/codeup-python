# n이 입력되면 크기가 n인 다음과 같은 2차원 배열을 출력하시오.

a = int(input())
b = [[0]*a for i in range(a)]
c = 0

for i in range(a):
    for j in range(a):
        c += 1
        b[j][i] = c

# for i in b:
#     # print(i, end=" ")
#     if i % a == 0:
#         print(i)
#     else:
#         print(i, end=" ")
for i in range(a):
    for j in range(a):
        print(b[i][j], end=" ")
    print()
