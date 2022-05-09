# 영어 공부에 빠져 있는 주현이는 영어 책을 자주 본다.
# 어느 날 영어 문장을 보면서 어떤 알파벳 문자가 많이 사용되는지 궁금해졌다.
# 영어 문장이 주어지면 a부터 z까지 알파벳 문자가 각각 몇 번 나왔는지 출력하는 프로그램을 작성하시오.

# a = input()
# a = list(a)
# b = []
# c = []
# for i in range(ord('a'), ord('z')+1):
#     b.append(chr(i))
# # print(b)
#
# for i in range(len(a)):
#     for j in range(len(b)):
#         if a[i] == b[j]:
#             c.append(1)
#
# for k in range(len(c)):
#     print(b[i], ":", c[i])

a = input()
b = [0 for i in range(26)]
for i in a:
    if 'a' <= i <= 'z':
        b[ord(i) - 97] += 1

for i in range(26):
    print("%c:%d" % (chr(i + 97), b[i]))
