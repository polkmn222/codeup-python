"""
세 정수가 입력되면 평균을 출력하시오.
"""
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
d = float((a + b + c) / 3)
print(format(d,".2f"))
