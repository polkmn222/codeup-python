"""
보림이는 엄마와 함께 놋데리아에 갔다.

보림이는 먹고 싶은게 많았으나 엄마가 살찐다고 2가지만 골라서 먹으라고 했다.

그리고 2메뉴의 칼로리 합이 500보다 크면 엄마가 화를 내고, 500이하면 화를 내지 않으신다.

보림이가 선택할 수 있는 메뉴는 다음과 같다.

1. 치즈버거 : 400 칼로리

2. 야채버거 : 340 칼로리

3. 우유 : 170 칼로리

4. 계란말이 : 100 칼로리

5. 샐러드 : 70 칼로리

이 메뉴들 중 2가지 메뉴를 선택했을 때 칼로리 합을 계산하고, 그 칼로리 합이 500보다 크면 "angry", 500이하면 "no angry"를 출력하시오.
"""
a, b = input().split()
a = int(a)
b = int(b)

c = 0
d = 0

if a==1:
    c += 400
elif a==2:
    c += 340
elif a==3:
    c += 170
elif a==4:
    c += 100
else:
    c += 70

if b==1:
    d += 400
elif b==2:
    d += 340
elif b==3:
    d += 170
elif b==4:
    d += 100
else:
    d += 70    

if c+d>500:
    print("angry")
else:
    print("no angry")
    