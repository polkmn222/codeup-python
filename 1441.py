# 버블 정렬은 '인접한 두 원소를 검사하여 자리를 바꿔가며 정렬하는 방식'이다.
# 이번 문제는 미리 작성된 코드를 보고 빈 칸에 들어갈 코드를 작성하는 것이다.
# 이 프로그램은 버블 정렬을 구현한 것이며, 실행 결과는 오름차순으로 정렬된다.

a = int(input())
b = []
for i in range(a):
    b.append(int(input()))
b.sort()
for i in range(a):
    print(b[i])