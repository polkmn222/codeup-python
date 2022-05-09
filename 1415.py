# 자연수는 홀수와 짝수로 나눌 수 있다.
# 10개의 자연수가 주어질 때, 홀수들 중 가장 큰 수와 짝수들 중
# 가장 큰 수를 구하여 출력하는 프로그램을 작성하시오. (단 모든 수가 홀수 혹은 짝수라면 가장 큰 수만 출력한다.)

a = list(map(int, input().split()))
b = 0
c = 0

for i in a:
    if i % 2 == 0:
        if i > b:
            b = i
    else:
        if i > c:
            c = i

if c != 0:
    print(c, end=" ")
if b != 0:
    print(b, end="")
