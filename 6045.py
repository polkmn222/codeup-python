"""
정수 3개를 입력받아 합과 평균을 출력해보자.
"""
a, b, c = input().split()
d = int(a) + int(b) + int(c)
e = d / 3
print(d, format(e, '.2f'), sep =' ')
