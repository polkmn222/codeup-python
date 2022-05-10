# *주의사항 : 이 (함수 제출형) 문제는 함수 부분만 작성해서 제출해야 오류 없이 채점이 됩니다.
# 미리 작성되어있는 코드를 읽고 해석해서, 함수 부분만 작성해서 제출하면 됩니다.
# 작성한 함수의 테스트를 위해서는 제시된 코드를 복사해 사용하면 되고, 제출은 함수 부분만 하세요.
#
# ------
#
# n 개의 정수를 배열로 입력 받고,
# 원하는 값 k가 저장되어있는 가장 처음 위치를 출력하시오.
# (원하는 값 k값이 저장되어있지 않은 경우에는 –1을 출력한다.)

def hello():
    a = int(input())
    b = list(map(int, input().split()))
    c = int(input())
    # print(a)
    # print(b)
    # print(c)
    for j in range(len(b)):
        if b[j] == c:
            return j+1
    return -1

    # a = int(input())
    # b = list(map(int, input().split()))
    # # b = []
    # # for i in range(a):
    # #     c = int(input())
    # #     b.append(c)
    # d = int(input())
    # for j in b:
    #     if j == d:
    #         print(j)
    #         break
    # for j in b:
    #     if j != d:
    #         print(-1)


print(hello())
