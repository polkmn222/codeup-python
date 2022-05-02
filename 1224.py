"""
분수의 크기를 비교하는 프로그램을 작성하시오.

분수는 a / b  , c / d 모양으로 주어진다.
"""
a,b,c, d = input().split()
a = int(a) 
b = int(b)
c = int(c)
d = int(d)

a1 = a/b
a2 = c/d

if a1>a2:
    print(">")
elif a1<a2:
    print("<")
else:
    print("=")
