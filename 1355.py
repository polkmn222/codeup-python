# 길이 n이 입력되면 다음과 같은 역삼각형을 출력한다.
#
# 예)
#
# n이 5이면
#
# *****
#  ****
#   ***
#    **
#     *

a = int(input())

# for i in range(a):
#     print(" " * i, end="")
#     for j in range(a, 1, -1):
#         print("*" * j, end="")
#     print()
# for i in range(a, 1, -1):
# for i in range(a, 0, -1):
#     # print("=", end="")
#     # print("%", end="")
#     for k in range(i-1, 0, -1):
#         print("%", end="")
#     for j in range(i, 0, -1):
#         print("*", end="")
#     # for k in range(i-1, 0, -1):
#     #     print("%", end="")
#     print()
for i in range(0, a):
    for j in range(0, i):
        print(' ', end='')
    for k in range(0, a-i):
        print('*', end='')
    print()