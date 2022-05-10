# *주의사항 : 이 (함수 제출형) 문제는 함수 부분만 작성해서 제출해야 오류 없이 채점이 됩니다.
# 미리 작성되어있는 코드를 읽고 해석해서, 함수 부분만 작성해서 제출하면 됩니다.
# 작성한 함수의 테스트를 위해서는 제시된 코드를 복사해 사용하면 되고, 제출은 함수 부분만 하세요.
#
# ------
#
# 다음과 같이, 점수를 입력 받아 학점을 출력하시오.
#
# 90 점 이상 ~ 100점 이하 : A
# 80 점 이상 ~ 90점 미만 : B
# 70 점 이상 ~ 80점 미만 : C
# 60 점 이상 ~ 70점 미만 : D
# 60 점 미만 : F

def grade(num):
    if 90 <= num <= 100:
        return 'A'
    elif 80 <= num < 90:
        return 'B'
    elif 70 <= num < 80:
        return 'C'
    elif 60 <= num < 70:
        return 'D'
    else:
        return 'F'


a = int(input())
print(grade(a))