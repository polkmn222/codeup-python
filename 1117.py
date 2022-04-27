"""
두 실수를 입력받아 두 실수의 곱을 출력하되 소수 둘째자리까지 출력하시오.
"""
a, b = input().split()
a = float(a)
b = float(b)
print(round(a*b, 2))
