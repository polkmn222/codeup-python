# 수의 개수 n이 주어지고, 그 다음 줄에 무작위로 n개의 자연수가 입력된다.
# 그 n개의 수 중에서 5의 배수만 골라 합을 출력하시오.

a = int(input())
num = list(map(int, input().split()))
total = 0

for i in range(len(num)):
    if num[i] % 5 == 0:
        total += num[i]
print(total)


