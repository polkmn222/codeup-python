# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최대값을 찾고 그 최대값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

# a = list(map(int, input()))
# print(a)
a = []

for i in range(0, 9):
    b = int(input())
    a.append(b)

# print(a)

c = 0
d = 0
# for j in range(0, 9):
#     for k in range(0, 9):
#         if a[k] > a[j]:
#             c = a[k]
#             d = k+1
#             continue
for j in range(len(a)):
    # for k in range(len(a)):
    if a[j] > c:
        c = a[j]
        d = j + 1
        # continue

print(c)
print(d)
