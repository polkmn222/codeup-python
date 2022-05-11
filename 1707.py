# 10명의 프로그래밍 점수를 입력받은 후, 점수의 평균을 구하여 평균보다 높은 사람과 낮은 사람이 각각 몇 명인지 구하는 프로그램을 작성하시오.
#
# (평균과 같은 사람은 평균보다 높은 사람에 포함시킨다.)

a = list(map(int, input().split()))
b = sum(a) / len(a)
print('%.1f' % b)
c = 0
d = 0
for i in range(len(a)):
    if a[i] < b:
        d += 1
    else:
        c += 1
print(c, d)
