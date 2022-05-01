"""
정수 하나를 입력받아 양수이면 "양수", 음수이면 "음수", 0이면 0을 출력하시오.
"""
a = int(input())

if a==0:
    print(0)
elif a>=0:
    print("양수")
else:
    print("음수")
