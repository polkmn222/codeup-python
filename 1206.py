"""
두 자연수 a, b가 주어진다.

b가 a의 배수이면 "a*x=b"를 출력하고,

a가 b의 배수이면 "b*x=a"를 출력하고,

배수관계가 아니면 "none"을 출력하시오.

예) 

5 10    ====> 5*2=10

14 2   ======> 2*7=14

3 7 =====> none
"""
a, b = input().split()
a = int(a)
b = int(b)
c = int(b/a)
if b%a==0:
    print(str(a)+"*"+str(c)+"="+str(b))
else:
    print("none")
