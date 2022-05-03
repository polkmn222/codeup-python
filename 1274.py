# 소수란, 약수가 1과 자기 자신 두 개 뿐인 수를 말한다.
#
# 어떤 수가 입력되면 그 수가 소수인지 판단하시오.

a = int(input())
b = 0
for i in range(1, a+1):
    if a % i == 0:
        b += 1

if b == 2:
     print("prime")
else:
    print("not prime")