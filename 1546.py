# *주의사항 : 이 (함수 제출형) 문제는 함수 부분만 작성해서 제출해야 오류 없이 채점이 됩니다.
# 미리 작성되어있는 코드를 읽고 해석해서, 함수 부분만 작성해서 제출하면 됩니다.
# 작성한 함수의 테스트를 위해서는 제시된 코드를 복사해 사용하면 되고, 제출은 함수 부분만 하세요.
#
# ------
#
# 정수 1개를 입력 받아
# 양수인 경우 plus, 음수인 경우 minus, 0 인 경우 zero를 판별하여 출력하시오.

def hello(a):
    if a == 0:
        return "zero"
    elif a > 0:
        return "plus"
    else:
        return "minus"

a = int(input())
print(hello(a))