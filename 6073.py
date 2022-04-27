"""
정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.
"""
a = int(input())
while a!=0:
    print(a-1)
    a = a-1
    if a==0: break
