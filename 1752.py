# 20글자 이하의 한 단어가 입력되면 뒤집어 출력하시오.

a = input()
a = list(a)
a.reverse()
for i in range(len(a)):
    print(a[i], end="")