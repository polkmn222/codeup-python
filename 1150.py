"""
세 정수가 주어지면 그 중 가장 작은 수를 출력한다.
"""
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

d = (a if a<b else b) if ((a if a<b else b)<c) else c
print(d)
