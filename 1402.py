# 두 수를 거꾸로 출력하기..
# 세 수를 거꾸로 출력하기...
# 이런 문제들은 쉽게 풀 수 있었다.
# 이번에는 데이터의 개수가 n개가 들어오고, n개의 데이터를 거꾸로 출력하는 프로그램을 작성하시오.

a = int(input())
b = list(map(int, input().split()))

# print(a)
# print(b)
# for i in range(a, 1, -1):
#     print(b[i], end=" ")

for i in range(a-1, -1, -1):
    print(b[i], end=" ")
