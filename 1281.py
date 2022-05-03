# 자연수 a, b 사이의 구간에 대해서 홀수는 더하고 짝수는 빼는 식을 보여준 후 결과를 출력하시오.

a , b = input().split()
a = int(a)
b = int(b)
num = list(range(a, b+1))
total = 0

for i in range(a, b+1):
    if i % 2 == 0:
        total -= i
    else:
        total += i

for i in range(len(num)):
    if num[i] % 2 == 0:
        num[i] = "-"+str(num[i])
        print(num[i], end="")
    else:
        if num[0] == num[i]:
            num[0] = num[i]
            print(num[0], end="")
        else:
            num[i] = "+"+str(num[i])
            print(num[i], end="")
print("="+str(total))