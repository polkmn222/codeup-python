"""
희윤이는 '성문이 두마리 치킨' 가게를 운영하고 있다.

치킨집을 운영하다 보니 매일 치킨을 먹게 되었다.

그러던 어느 날 몸무게를 재어보니 80kg이 나가는 것을 보고 깜짝 놀랐다.

희윤이 여자친구는 비만인 사람을 제일 싫어 하므로 희윤이는 절대 비만이면 안 된다.

희윤이가 비만인지 아닌지 판별하는 프로그램을 작성하시오.


* 비만도 계산 공식(브로카의 공식)

항목	공식
표준몸무게 = 	(실제 키 - 100) * 0.9
비만도 = 	
(실제 몸무게 - 표준몸무게)  * 100 / 표준 몸무게

* 비만도에 따른 등급 판정

등급	비만도 수치
10 이하	정상
10~20 이하	과체중
20 초과	비만
"""
a, b = input().split()
a = float(a)
b = float(b)
c = (a-100)*0.9
# print(c)
d = (b-c)*100/c
# print(d)

if d<=10:
    print("정상")
elif d<=20:
    print("과체중")
else:
    print("비만")
