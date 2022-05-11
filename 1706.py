# 5개의 데이터를 입력받아 거꾸로 출력하는 프로그램을 작성하시오.

a = list(map(int, input().split()))
b = a.reverse()
# a = a.reverse()
for i in range(len(a)):
    print(a[i], end=" ")
# print(b)