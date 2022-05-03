# 두 자연수 a, b 사이의 구간에 대해서
#
# 홀수는 더하고 짝수는 빼는 식을 보여준 후 결과를 출력하시오.
#
# 단, 결과가 양수이면 +를 붙이지 않는다.

a , b = input().split()
a = int(a)
b = int(b)
num = list(range(a, b+1))
total = 0
# print(num)
"""
for i in range(b-a):
    num[i] = i
    print(num[i])
"""

for i in range(a, b+1):
    if i % 2 == 0:
        total -= i
    else:
        total += i
    # print(i)

# print(total)
for i in range(len(num)):
    if num[i] % 2 == 0:
        num[i] = "-"+str(num[i])
        print(num[i], end = "")
    else:
        num[i] = "+"+str(num[i])
        print(num[i], end = "")
print("="+str(total))