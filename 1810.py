# 어떤 문자열에서 부분문자열을 추출하여 출력하는 프로그램을 작성하시오.
#
# 단 배열 대신 동적메모리 할당방법을 사용하시오.

a = input()
a = list(a)

b, c = input().split()
b = int(b)
c = int(c)

for i in range(len(a)):
    if i == b:
        for j in range(b-1, c):
            print(a[j], end="")
    # if i == c:
    #     print(i)
if b == 1 and c == 1:
    for i in range(len(a)):
        print(a[i])