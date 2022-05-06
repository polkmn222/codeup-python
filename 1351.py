# 시작단과 마지막 단을 입력하면
# 그 구간의 구구단을 출력하는 프로그램을 작성하시오.

a, b = input().split()
a = int(a)
b = int(b)

for n in range(a, b+1):
    for i in range(1, 10):
        print(f'{n}*{i}={n*i}')

