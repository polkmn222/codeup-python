# 길이 n이 입력되면 역삼각형을 출력한다.
#
# 예)
#
# n이 5이면
#
# *****
# ****
# ***
# **
# *

a = int(input())

for i in range(a, 0, -1):
    print("*" * i)