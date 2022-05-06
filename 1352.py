# 길이 n이 입력되면 길이가 n인 사각형을 출력하시오.
# 단, 사각형은 * 모양으로 채운다.

a = int(input())

for i in range(a):
    print("*", end="")
    for j in range(1, a):
        print("*", end="")
    print()