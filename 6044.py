"""
정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산해보자.
단, b는 0이 아니다.
"""
a, b = input().split()
c = int(a) + int(b)
d = int(a) - int(b)
e = int(a) * int(b)
f = int(a) / int(b)
g = int(a) % int(b)
h = int(a) // int (b)
print(c)
print(d)
print(e)
print(h)
print(g)
print(format(f, '.2f'))
