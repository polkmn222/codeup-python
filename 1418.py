# 어떤 문자열이 있을 때 문자 t의 위치를 모두 찾아 출력하시오.

a = input()
a = list(a)

# for i in a:
#     if i == 't':
#         print(i, end=" ")

for i in range(len(a)):
    if a[i] == 't':
        print(i+1, end=" ")