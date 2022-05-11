# 희용이는 for문을 공부하다가 다음과 같은 프로그램을 생각해냈다.
#
# a부터 b까지의 수 중에서 3의 배수는 더하고, 4의 배수는 빼는 프로그램을 만들어 보자.
#
# 만약 그 수가 3과 4의 공배수라면 더하거나 빼는 것을 생략한다.

a, b = input().split()
a = int(a)
b = int(b)
c = 0
for i in range(a, b+1):

    if i % 3 == 0 and i % 4 == 0:
        c += 0
    elif i % 4 == 0:
        c -= i
    elif i % 3 == 0:
        c += i
    # print(c)
print(c)