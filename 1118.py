"""
삼각형의 넓이를 구하는 프로그램을 작성한다.

삼각형의 넓이 = 밑변 * 높이 / 2
"""

a, b = input().split()
a = int(a)
b = int(b)
c = a * b / 2
print(c)
