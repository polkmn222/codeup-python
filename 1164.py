"""
어떤 차의 높이가 170cm 이다.

이 차는 3개의 터널을 차례대로 지나게 될 것이다.

터널의 높이가 차의 높이보다 같거나 낮다면 차는 터널과 충돌하여 사고가 날 것이다.

터널의 높이가 차례대로 3개 주어지면 터널을 무사히 잘 통과하면 PASS 를 출력하고, 사고가 난다면 CRASH 를 출력하시오.
"""
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a<=170 or b<=170 or c<=170:
    print("CRASH")
else:
    print("PASS")
