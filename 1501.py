# n이 입력되면 크기가 n인 다음과 같은 2차원 배열을 출력하시오.

a = int(input())
b = []

for i in range(a*a):
    b.append(i+1)

for i in b:
    print(i, end=" ")
    if i % a == 0:
        print()
