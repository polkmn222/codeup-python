# n개의 숫자가 입력되면,
# n개의 숫자를 왼쪽으로 하나씩 돌려서 출력하시오.
# 예) 1 2 3 4 5가 입력된 경우,
# 1 2 3 4 5
# 2 3 4 5 1
# 3 4 5 1 2
# 4 5 1 2 3
# 5 1 2 3 4

a = int(input())
b = list(map(int, input().split()))

for i in range(a):
    for j in range(i, len(b)):
        print(b[j], end=" ")

    for k in range(0, i):
        print(b[k], end=" ")

    print()

