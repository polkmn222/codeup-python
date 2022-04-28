"""
10진수 정수를 입력받아 8진수와 16진수로 출력한다.
"""
a = int(input())
b = format(a, 'o')
c = format(a, 'X')
print(b, c)
