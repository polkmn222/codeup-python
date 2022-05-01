"""
학번을 입력 받아 다음 형식으로 출력하시오.

학번은 학년, 반, 번호로 입력된다.

예)

2 3 27   =====>    2327로 출력

2 3 7   ======> 2307로 출력   (번호가 10번미만이면 0을 붙여 출력)
"""
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
if c<10:
    print(str(a)+str(b)+"0"+str(c))
else:
    print(str(a)+str(b)+str(c))
