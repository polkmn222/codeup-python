"""
학번을 입력 받아 다음 형식으로 출력하시오.

학번은 학년, 반, 번호로 입력된다.

이번에는 학년은 한자리, 반은 두자리, 번호는 세자리로 출력한다.

예)

2 1 20  ===> 201020  으로 출력

2 2 7 ==> 202007 으로 출력

2 3 100 ==>  203100 으로 출력

2 10 111 ==> 210111 로 출력
"""
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
"""
if b<10 and c<100:
    print(str(a)+"0"+str(b)+"0"+str(c))
elif b<10:
    print(str(a)+"0"+str(b)+str(c))
elif c<100:
    print(str(a)+str(b)+"0"+str(c))
else:
    print(str(a)+str(b)+str(c))
"""
#print(format("%d"%a,"%02d"%b,"%03d"%c))
print('{0}{1:02d}{2:03d}'.format(a, b, c))
