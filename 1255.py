"""
소수 둘째 자리의 두 실수 a와 b가 입력으로 주어진다.

a와 b사이의 수를 0.01간격으로 오름차순으로 출력하시오.
"""
a,b = input().split()
a = float(a)
b = float(b)

"""
for i in range(a,b+0.01,0.01):
    print(i, end = "")
"""
while(a<=b):
    print(format(a,".2f"), end = " ")
    a = a+0.01
