# 두 자연수 a, b 사이의 구간에 대해서
#
# 홀수는 더하고 짝수는 뺀다음의 합을 출력하시오.

a , b = input().split()
a = int(a)
b = int(b)
total = 0
for i in range(a, b+1):
    if i % 2 == 0:
        total -= i
    else:
        total += i

print(total)