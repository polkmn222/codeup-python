"""
시작수와 마지막 수가 입력되면

시작수부터 마지막 수까지의 모든 홀수를 출력하시오.
"""
a,b = input().split()
a = int(a)
b = int(b)

for i in range(a,b+1):
    if i%2==0:
        continue
    print(i, end=" ")
    
