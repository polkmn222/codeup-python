"""
영어로 서수를 표현할 때 다음과 같이 나타낸다.

1st  2nd  3rd  4th  5th  6th  ... 10th

11th 12th 13th 14th 15th  ...  20th

21st 22nd 23rd 24th 25th  ...  30th

31st 32nd 33rd 34th 35th  ...  40th

41st 42nd 43rd 44th 45th  ...  50th

...

91st 92nd 93rd 94th 95th  ...  99th

1~99 중 하나가 숫자가 입력되면 영어 서수 표현을 출력하시오.
"""
a = int(input())

if a==1 or a%10==1:
    if a==11:
        print(str(a)+"th")
    else:
        print(str(a)+"st")
elif a==2 or a%10==2:
    if a==12:
        print(str(a)+"th")
    else:
        print(str(a)+"nd")
elif a==3 or a%10==3:
    if a==13:
        print(str(a)+"th")
    else:
        print(str(a)+"rd")
else:
    print(str(a)+"th")
    
