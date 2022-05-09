# 길이가 100 이하인 문자열로 구성된 암호문을 발견하였다.
# 이 암호문은 예전에 작성된 것으로 판단된다.
# 이 문자열에서 “C”라는 문자와 “CC”라는 문자가 몇 개 있는지 조사하고자 한다.
# 길이가 100 이하인 문자열을 입력받아, "C"라는 문자와 "CC"라는 문자가 각각 몇 개 존재하는지 알아내는 프로그램을 작성하시오. (단, C, CC는 대소문자를 구분하지 않는다. 즉, "cC"는 "CC"와 같다.)

# a = input()
# b = ''
# d = 0
# f = 0
#
# for i in a:
#     c = ord(i)
#     # print(chr(c))
#
#     if c == ord('c') or c == ord('C'):
#         d += 1
#     if i != len(a)-1 and len(a+1) == 'C':
#         # if c == (ord('c') or ord('C')) and (ord('c') or ord('c'))\
#         #         and (ord('C') or ord('C')) and (ord('c') or ord('c')):
#         f += 1
# print(d)
# print(f)

a = input()
a = a.upper()
b = 0
c = 0

for i in range(0, len(a)):
    if a[i] == 'C':
        b += 1
        if i != len(a)-1 and a[i+1] == 'C':
            c += 1

print(b)
print(c)
# print(type(a))

