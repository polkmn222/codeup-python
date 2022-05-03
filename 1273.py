# 자연수 N이 주어 지면 N의 약수를 오름차 순 으로 모두 출력 하시오.
a = int(input())

for i in range(1, a+1):
    if a % i == 0:
        print(i, end=" ")
