"""
정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.
"""
a = int(input())
total = 0
for i in range(a+1):
    if i%2 ==0:
        total += i

print(total)        
