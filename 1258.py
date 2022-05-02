"""
정수 n이 입력으로 들어오면 1부터 n까지의 합을 구하시오.
"""
a = int(input())
num = 0
for i in range(1, a+1):
    num +=i
print(num)    
