# 데이터를 입력받아 내림차순으로 정렬하는 프로그램을 작성하시오.

a = int(input())
b = list(map(int, input().split()))

# print(b)
# print(type(b))
# b = b.sort()
# sorted(b)
# print(b)
# sorted(b, key=lambda c: b[0])
b.sort(reverse=True)
# print(b)

# for i in range(len(b)):
#     print(b[i], end=" ")

for i in range(len(b)):
    print(b[i], end=" ")