"""
1부터 n까지의 수 중 짝수의 합을 구하시오.
"""
a = int(input())
num = 0
for i in range(1, a+1):
    if i%2!=0:
        continue
    num +=i
print(num)    
