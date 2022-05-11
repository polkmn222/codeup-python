# 학생의 점수를 입력받아 순위를 구하는 프로그램을 작성하시오.
#
# 동점자의 경우 같은 순위를 부여한다.
#
# (예를 들어, 85 100 85 74 점이면, 2등 1등 2등 4등 과 같이 순위가 매겨진다.)

a = int(input())
b = list(map(int, input().split()))
c = 1

for i in range(len(b)):
    for j in range(len(b)):
        if b[i] < b[j]:
            c += 1

    print(b[i], c)
    c = 1