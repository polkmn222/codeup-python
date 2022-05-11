# 용준이와 봉찬이는 분수를 아는 학생이다.ㅋ
#
# 분수 공부를 하다가 기약분수로 만드는 프로그램을 만들기로 했다.
#
# 분자, 분모가 입력되면 기약분수의 형태로 출력하는 프로그램을 작성하시오.
#
# ※ 기약분수 : 더 이상 약분할 수 없는 분수이다.
#
# 예를 들어 5 / 25 를 기약분수로 바꾸면 1 / 5 이다.
#
# 5     5로 나눈다      1
# ---  ---------------->  ---
# 25    5로 나눈다      5
# 이 순서로 으로 기약분수가 된다.

def hello():

    a, b = input().split()
    a = int(a)
    b = int(b)

    if b % a == 0:
        return print(1, int(b/a))

    for i in range(int(a/2), 1, -1):
        if b % i == 0 and a % i == 0:
            return print(int(a/i), int(b/i))

    return print(a, b)


hello()
