# 영어 문장이 입력된다.
# 그 문장에서 love가 몇 번 나오는지 출력하시오.

a = input()
b = 0
for i in range(len(a)):
    if a[i] == 'l':
        if a[i+1] == 'o':
            if a[i+2] == 'v':
                if a[i+3] == 'e':
                    b += 1
print(b)