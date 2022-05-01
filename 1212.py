"""
세 개의 직선이 있다.

숫자의 의미는 직선의 길이를 말한다.

이 직선으로 삼각형을 만들 수 있는지 판단하는 프로그램을 작성하시오.

삼각형의 성립 조건)

a, b, c 가 변의 길이이고 c가 제일 긴 길이라고 한다면

c < a + b 이면 삼각형이 성립됨.
"""
a, b,c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a>b and a>c:
    if b+c > a:
        print("yes")
    else:
        print("no")
elif b>a and b>c:
    if a+c > b:
        print("yes")
    else:
        print("no")
else:
    if a+b > c:
        print("yes")
    else:
        print("no")
