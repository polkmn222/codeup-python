# 프로그래밍을 할 때 가장 중요한 것 중 하나가 괄호의 개수를 맞추는 것이다.
# 즉, 여는 괄호가 있으면 항상 닫는 괄호가 있고, 닫는 괄호가 있으면 여는 괄호도 있어야 한다.
# 올바른 괄호를 확인하기 위해 가장 기본적인 방법 중 하나는 여는 괄호와 닫는 괄호의 개수를 세는 것이다.
# 소괄호로 이루어진 문자열을 주어지면 괄호의 개수를 출력하는 프로그램을 작성하시오.

# a = list(map(str, input().split()))
a = input()
b = ''
c = ''
d = 0
e = 0


for i in a:
    b = ord(i)
    if b == 40:
        d += 1
    elif b == 41:
        e += 1
    # print(a[i], end="")
    # print()
# print(a[0])
print(d, e)