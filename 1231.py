"""
영민이는 프로그램을 이용하여 계산기를 만들려고한다.

하지만 영민이는 프로그램을 얼마 배우지 않아 어려워하고있다.

우리가 영민이를 위해 계산기 프로그램을 만들어주자.
"""
#num = list(map(str,input().split()))

#print(num)
"""
a,b,c=num.split("")
a = int(a)
b = str(b)
c = int(c)

if b=="+":
    print(a+c)
elif b=="-":
    print(a-c)
elif b=="*":
    print(a*c)
elif b=="/":
    print(format(a/c,".2f"))
"""
num = input()
#print(num[0])
for i in range(len(num)):
    if num[i]=="+":
        a , c = num.split("+")
        b = "+"
    elif num[i]=="-":
        a , c = num.split("-")
        b = "-"
    elif num[i]=="*":
        a , c = num.split("*")
        b = "*"
    elif num[i]=="/":
        a , c = num.split("/")
        b = "/"    

#print(a,b,c)
a = int(a)
c = int(c)

if b=="+":
    print(a+c)
elif b=="-":
    print(a-c)
elif b=="*":
    print(a*c)
elif b=="/":
    print(format(a/c,".2f"))      
