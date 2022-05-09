# n 행 m열의 2차원 배열에 값을 저장하고 출력하려고 한다.
# 첫째 줄에 2차원 배열의 크기 n과 m을 입력받고,
# 각각의 데이터를 2차원 배열에 저장한 다음 그대로 출력하시오.

# a, b = input().split()
# a = int(a)
# b = int(b)
# c = [[a, b]]
# d = []
# for i in range(a):
#     c.append(map(int, input().split()))
# for i in range(b):
#     d.append(map(int, input().split()))
# d.append(input().split())
# for i in range(0, a):
#     for j in range(0, b):
#         print(c[[i, j]], end=" ")
#     print()
# for i in d:
#     print(i, end=" ")

a, b = map(int, input().split())
c = []

for i in range(0, a):
    d = list(map(int, input().split()))
    c.append(d)

for i in range(0, a):
    for j in range(0, b):
        print(c[i][j], end=' ')
    print()