# 오름차순 삽입 정렬은 '정렬된 데이터 셋에 뒤쪽에서 부터 원소를 하나씩 삽입하여 순서에 맞는 위치로 찾아가며 정렬하는 방식'이다.
# 이번 문제는 미리 작성된 코드를 보고 빈 칸에 들어갈 코드를 작성하는 것이다.
# 이 프로그램은 선택 정렬을 구현한 것이며, 실행 결과는 오름차순으로 정렬된다.

a = int(input())
b = []
for i in range(a):
    b.append(int(input()))
b.sort()
for i in range(a):
    print(b[i])