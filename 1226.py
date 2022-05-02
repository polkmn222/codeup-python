"""
지혜는 로또 매니아다.

매주 로또 한장을 사고 토요일이면 대박을 기대하면서 당첨번호를 확인한다.

지혜는 로또 결과가 4등이었는데 확인을 잘못해서 5등인줄 알고 그냥 바꾸기 귀찮아서 버렸었다.

(사실은 다른 줄에 있는 것까지 합쳐서 3개 맞았는데 5등인줄 알았다고 한다.)

이러한 사태가 다시는 일어나지 않게 하기 위해 우리가 프로그램을 만들어 주자.

로또 순위 매기는 방법)

등수	방법
1등	당첨번호 6개 일치
2등	당첨번호 5개 일치 + 보너스번호 일치
3등	5개 번호 일치
4등	4개 번호 일치
5등	3개 번호 일치
꽝	2개 이하 일치

예)

13 23 24 35 40 45 7     ===> 로또 당첨번호 + 보너스 번호

 2  6  7 23  40 44      ====> 지혜가 가진 로또 번호

따러서 지혜는 "꽝"
"""
"""
a,b,c,d,e,f,g = input().split()
a1,b1,c1,d1,e1,f1 = input().split()

arr =
"""
num = list(map(int,input().split()))
#print(num)
arr = list(map(int,input().split()))
total = 0
luck = 0
for i in range(len(num)):
    for j in range(len(arr)):
        if num[i]==arr[j]:
            if num[6]==arr[j]:
                luck += 1
            else:
                total += 1
"""    
            total += 1
            continue
    if num[6]==arr[j]:
        luck += 1
        total -=1
        continue
"""            
#print(total)        
if total==6:
    print(1)
elif total ==5 and luck==1:
    print(2)
elif total==5:
    print(3)
elif total==4:
    print(4)
elif total==3:
    print(5)
else:
    print(0)
