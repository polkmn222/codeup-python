"""
세 정수가 주어지면 그 중 가장 작은 수를 출력한다.
"""
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

"""
if a>b and b>c:
    print(c)
elif c>a and a>b:
    print(b)
elif c>b and b>a:
    print(a)
"""
if a>b:
    if b>c:
        print(c)
elif b>c:
    if c>a:
        print(a)
elif c>a:
    if a>b:
        print(b)
elif a>c:
    if c>b:
        print(b)
elif b>a:
    if a>c:
        print(c)
elif c>b:
    if b>a:
        print(a)        
