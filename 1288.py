# nCr은 n개의 원소를 가지는 집합에서 r개의 부분 집합을 고르는 조합의 수를 말한다.
#
# nCr을 일반 공식은 다음과 같다.
#
# nCr=nPrr!=n!r!⋅(n−r)!
# 5C2는 다음과 같이 구할 수 있다.
#
# 5C2=5!3!×2!=5×4×3×2×1(3×2×1)×(2×1)=10
# nCr을 구하는 프로그램을 작성하시오.

a, b = input().split()
a = int(a)
b = int(b)

num = 1
for i in range(a, 1, -1):
    num *= i
    # print(num)
# print(num)
num1 = 1
num2 = 1
# print(num1)
for j in range(a-b, 1, -1):
    num1 *= j
    # print(num1)

for k in range(b, 1, -1):
    num2 *= k

# print(num, num1, num2)
c = int(num / (num1 * num2))
print(c)