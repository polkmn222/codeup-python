# 두 정수 n과 k가 입력된다.
#
# n을 k진법으로 변환한 결과를 출력하시오.

#
#
# def toN(n, num=2):
#     res=[]
#     res2=''
#     while n>0:
#         n, tmp = divmod(n, num)
#         res.append((str(tmp) if tmp <10 else 'ABCDEF'[tmp-10]))
#
#     for i in range(len(res)):
#         res2 += res.pop()
#
#     return res2
#
#
# print(toN(a, b))
# c = []
def form(n):
    if n < 10:
        return chr(n + 48)
    else:
        return chr(n + 55)


#
#

a, b = input().split()
a = int(a)
b = int(b)
c = []

for i in range(28):
    if a / b == 0:
        c.append(form(a))
        a = i
        break
    # c.append(form(int(a % b)))
    c.append(form(int(a%b)))
    a /= b
    a = int(a)
# print(type(a))
# print((a))
# a = int(a)
for j in range(len(c)-1, 0, -1):
    print(c[j-1], end="")
# for j in reversed(a):
#     print(c[j])
# print(c)
if a == 0 :
    print(0)