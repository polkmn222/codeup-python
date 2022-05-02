"""
어떤 수 a, b가 주어진다.

a와 b의 관계는 a <= b 이다.

a에서 b까지의 수 중 3의 배수만 더하여 출력하시오.
"""
a, b = input().split()
a = int(a)
b = int(b)
total = 0
for i in range(a,b+1):
    if i%3==0:
        total += i
print(total)        
