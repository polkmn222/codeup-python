# *주의사항 : 이 (함수 제출형) 문제는 함수 부분만 작성해서 제출해야 오류 없이 채점이 됩니다.
# 미리 작성되어있는 코드를 읽고 해석해서, 함수 부분만 작성해서 제출하면 됩니다.
# 작성한 함수의 테스트를 위해서는 제시된 코드를 복사해 사용하면 되고, 제출은 함수 부분만 하세요.
#
# ------
#
# prime 또는 composite 중 하나를 출력하시오.
def hello(a):
    b = 0
    for i in range(2, int(a/2)):
        if a % i == 0:
            print("composite")
            b += 1
            break
    if b == 0:
        print("prime")


a = int(input())
hello(a)