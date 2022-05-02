"""
삼각형의 3변의 길이 a, b, c가 입력으로 주어진다.

여기서 입력되는 변의 관계는 a ≤ b ≤ c 이다. 

그 삼각형이 무슨 삼각형인지 출력하시오.
"""
import math
a,b,c = input().split()
a = int(a) 
b = int(b)
c = int(c)


if a==b and b==c:
    print("정삼각형")
elif math.pow(a,2) + math.pow(b,2) == math.pow(c,2) or math.pow(a,2) + math.pow(c,2) == math.pow(b,2) or math.pow(c,2) + math.pow(b,2) == math.pow(a,2):
    print("직각삼각형")
elif a+b<=c or a+c<=b or b+c<=a:
    print("삼각형아님")
elif (a==b and a!=c) or (a==c and a!=b) or (c==b and c!=a):
    print("이등변삼각형")
else:
    print("삼각형")

                                                        
