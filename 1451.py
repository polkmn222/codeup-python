# 데이터 정렬은 프로그래밍 문제를 푸는데 많이 사용된다.
# N개의 데이터가 입력되면, 오름차순된 결과를 출력하는 프로그램을 작성하시오.
a = int(input())
b = []
for i in range(a):
    b.append(int(input()))
b.sort()
for i in range(a):
    print(b[i])