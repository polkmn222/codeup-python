# 정렬된 두 배열을 합쳐서 정렬하시오.

a, b = input().split()
c = list(map(int, input().split()))
d = list(map(int, input().split()))
e = c + d
e.sort()
# for i in e:
#     if i == '':
#         e.remove(i)
#     for j in e:
#         if j == '':
#             e.remove(j)
# # e.remove('')
for i in e:
    print(i, end=" ")
# print(e)