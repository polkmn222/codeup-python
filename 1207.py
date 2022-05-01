"""
윷놀이는 4개의 윷을 이용하는 게임이다.

 

도 : 1개가 뒤집어진 상태

개 : 2개가 뒤집어진 상태

걸 : 3개가 뒤집어진 상태

윷 : 4개가 뒤집어진 상태

모 : 하나도 뒤집어지지 않은 상태

 

4개의 윷 상태가 입력되면 도, 개, 걸, 윷, 모를 출력하는 프로그램을 작성하시오.
"""
a, b, c, d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
f = a + b + c + d
if f==1:
    print("도")
elif f==2:
    print("개")
elif f==3:
    print("걸")
elif f==4:
    print("윷")
else:
    print("모")
