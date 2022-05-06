# k개의 숫자를 입력받고 그 숫자들을 두번 출력하시오.
#
# 입력 예)
# 2
# 5 7
# 출력 예)
# 5
# 7
# 5
# 7

a = int(input())
b = list(map(int, input().split()))

# for i in range(2):
#     for j in range(len(b)):
#         print(b[i])

# for j in range(len(b)):
#     for i in range(2):
#         print(b[j])
for i in range(len(b)):
    print(b[i])

for j in range(len(b)):
    print(b[j])