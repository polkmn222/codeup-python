"""
** 3 6 9 게임은?
여러 사람이 순서를 정한 후, 순서대로 수를 부르는 게임이다.
만약 3, 6, 9 가 들어간 수를 자신이 불러야 하는 상황이라면, 수를 부르는 대신 "박수(X)" 를 쳐야 한다.
33과 같이 3,6,9가 두 번 들어간 수 일때, "짝짝"과 같이 박수를 두 번 치는 형태도 있다.
"""
a = int(input())
"""
for i in range(1, a+1):
    if(i==3 or i==6 or i==9 or i==13 or i==16 or i==19 or i==23 or i==26 or i==29):
        print('X', end =' ')
    else:
        print(i, end =' ')
"""

for i in range(1, a+1) :
  if i%10==3 or i%10==6 or i%10==9 :
    print("X", end=' ')
  else :
    print(i, end=' ')
