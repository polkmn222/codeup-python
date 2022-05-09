# *주의사항 : 이 (함수 제출형) 문제는 함수 부분만 작성해서 제출해야 오류 없이 채점이 됩니다.
# 미리 작성되어있는 코드를 읽고 해석해서, 함수 부분만 작성해서 제출하면 됩니다.
# 작성한 함수의 테스트를 위해서는 제시된 코드를 복사해 사용하면 되고, 제출은 함수 부분만 하세요.
#
# ------
#
# 배열에서 가장 큰 값이 처음 나타나는 위치를 출력하시오.


a = int(input())
b = list(map(int, input().split()))
c = 0


# for i in range(a):
# b.append(map(int, input().split()))
# for i in b:
#     if i > c:
#         c = i
# # print(c)
# # print(b)
# for i in range(len(b)):
#     if b[i] == c:
#         print(i + 1)
#         break
def hello(b):
    c = 0
    for i in b:
        if i > c:
            c = i

    for i in range(len(b)):
        if b[i] == c:
            d = (i + 1)
            break
    return d


print(hello(b))
