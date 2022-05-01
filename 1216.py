"""
대영이는 SNS를 이용한 컨설팅 회사를 운영하고 있다. 

이 회사에서 획기적인 기획안을 개발하여 사람들에게 홍보를 하려고 한다.

홍보를 할 경우 수입과 그렇지 않을 경우의 수입을 알고 있을 경우, 

홍보를 하는 경우가 유리한가?

홍보를 하지 않은 경우가 유리한가?

그것도 아니면 홍보를 하든 안하든 별 관계가 없는가?

이것을 알아내는 프로그램을 만드시오.
"""
a,b,c = input().split()
a = int(a) 
b = int(b)
c = int(c)

d = b-c
if d>a:
    print("advertise")
elif d<a:
    print("do not advertise")
else:
    print("does not matter")
