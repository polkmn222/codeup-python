"""
재호는 이번 시험에 받은 성적이 궁금했다.

점수가 입력되면 등급을 출력하시오.

등급)

 90점 이상 : A

80점 이상 : B

70점 이상 : C

60점 이상 : D

60점 미만 : F
"""
a = int(input())

if a>=90:
    print('A')
elif a>=80:
    print('B')
elif a>=70:
    print('C')
elif a>=60:
    print('D')
else:
    print('F')
