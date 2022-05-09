# N 개의 데이터가 입력되면, 오름차순된 결과를 출력하는 프로그램을 작성하시오.
a = int(input())
b = []
for i in range(a):
    b.append(int(input()))
b.sort()
for i in range(a):
    print(b[i])