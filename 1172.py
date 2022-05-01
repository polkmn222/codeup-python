"""
세 수를 오름차순으로 정렬하려고 한다. (낮은 숫자 -> 높은 숫자)

예)

5 8 2   ====> 2 5 8    로 출력
"""
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
#d = [a, b, c]
#d.sort()
#print(d)

if a>=b and a>=c:
    if b>=c:
        print(c,b,a)
    else:
        print(b,c,a)
elif b>=a and b>=c:
    if a>=c:
        print(c,a,b)
    else:
        print(a,c,b)
else:
    if a>=b:
        print(b,a,c)
    else:
        print(a,b,c)
            
