"""
수의 개수  n이 주어 지고, 그 다음 줄에 무작 위로 n개의 정수가 입력 된다.

n개의 수의 합을 출력 하시오.
"""
a = int(input())
num = list(map(int, input().split()))
total = 0
# for i in range(a):
#     num[i] = int(input())

for i in range(len(num)):
    # print(num[i], end=" ")
    total += num[i]
print(total)

