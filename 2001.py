# 파파 파스타 가게는 점심 추천 파스타와 생과일 쥬스 세트 메뉴가 인기가 좋다.
#
# 이 세트 메뉴를 주문하면 그 날의 3 종류의 파스타와 2 종류의 생과일 쥬스에서 하나씩 선택한다.
#
# 파스타와 생과일 쥬스의 가격 합계에서 10%를 더한 금액이 대금된다.
#
# 어느 날의 파스타와 생과일 쥬스의 가격이 주어 졌을 때, 그 날 세트 메뉴의 대금의 최소값을 구하는 프로그램을 작성하라.

a1 = int(input())
a2 = int(input())
a3 = int(input())
b1 = int(input())
b2 = int(input())

c1 = 0
c2 = 0
# a1 = a1 / 100 * 10 + a1
# a2 = a2 / 100 * 10 + a2
# a3 = a3 / 100 * 10 + a3
# a4 = a4 / 100 * 10 + a4
# a5 = a5 / 100 * 10 + a5
#
# b = a1 + a2 + a3 + a4 + a5
# print(b)

a = [a1, a2, a3]
b = [b1, b2]

for i in range(len(a)):
    if a[0] > a[1]:
        if a[1] > a[2]:
            sum1 = a[2]
        else:
            sum1 = a[1]
    elif a[1] > a[2]:
        if a[2] > a[0]:
            sum1 = a[0]
        else:
            sum1 = a[2]
    else:
        if a[0] > a[1]:
            sum1 = a[1]
        else:
            sum1 = a[0]

for j in range(len(b)):
    if b[0] > b[1]:
        sum2 = b[1]
    else:
        sum2 = b[0]

sum1 = sum1 + sum1/100*10
sum2 = sum2 + sum2/100*10
sum3 = sum1 + sum2
print("%.1f" % sum3)