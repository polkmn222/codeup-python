# 주어지는 문장의 대문자를 소문자로, 소문자를 대문자로 변경하는 프로그램을 작성하라.

a = input()
b = ''

for i in a:
    c = ord(i)

    if ord('A') <= c <= ord('Z'):
        c += 32
    elif ord('a') <= c <= ord('z'):
        c -= 32
    else:
        c = c
    b += chr(c)
print(b)


