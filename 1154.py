"""
정수 두개가 입력으로 들어오면 큰수 - 작은수의 값을 출력하시오.
"""
a, b = input().split()
a = int(a)
b = int(b)
if a>b:
    print(a-b)
else:
    print(b-a)
    
