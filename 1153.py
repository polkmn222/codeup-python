"""
두 정수가 입력된다.  두 정수의 크기를 비교하여 왼쪽 수가 크면 > 를 출력, 오른쪽 수가 크면 < 를 출력, 같으면 = 을 출력하시오.
"""
a, b = input().split()
a = int(a)
b = int(b)
if a>b:
    print(">")
elif a==b:
    print("=")
else:
    print("<")
