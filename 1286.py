# 5개의 정수들의 최댓값과 최솟값을 구하는 프로그램을 작성하라.

list1 = []

for i in range(5):
    a = int(input())
    list1.append(a)
# print(type(list1))
# print(list1[0])
b = -9999999

for i in range(len(list1)):
    if b <= list1[i]:
        b = list1[i]
print(b)

c = 9999999
for i in range(len(list1)):
    if c >= list1[i]:
        c = list1[i]
print(c)

