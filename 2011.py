# 시작 수(a)와 마지막 수(b)가 입력되면 그 범위의 369게임의 올바른 답을 출력하시오.
#
# ※ 369게임의 룰은 다음과 같다.
#
# 1. 시작수와 마지막수까지의 369게임의 올바른 답을 출력한다.
#
# 2. 한 줄에 하나의 결과를 출력한다.
#
# 3. 369에 해당될 경우 3이나 6이나 9가 들어간 개수만큼  "K"를 출력한다.
#
# 4. 그 외의 숫자들은 그냥 그대로 출력한다.

a, b = input().split()
a = int(a)
b = int(b)
total = 0


def sam(n):
    c = 0
    while n != 0:
        if n % 10 == 3 or n % 10 == 6 or n % 10 == 9:
            c += 1
        n /= 10
        n = int(n)
    return c


for i in range(a, b + 1):
    total = sam(i)
    if total == 0:
        print(i)
    else:
        for j in range(0, total):
            print("K", end="")
        print()
