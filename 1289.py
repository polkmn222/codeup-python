# 학교에서 축구대회를 열기로 했다. 본교 학생 수가 많아서 되도록 큰 운동장을 필요로 한다.
# 학교 근처에 축구를 할 수 있는 운동장이 3개가 있는데 각 운동장의 가로와 세로의 길이를 홈페이지를 통해서 알 수 있었다.
# 우리는 3개의 운동장 중 가장 큰 운동장을 빌리기로 했다.
# 이 3개의 운동장 중 가장 넓은 운동장의 넓이를 구하는 프로그램을 작성하시오.

list1 = []

for i in range(3):
    a , b = input().split()
    a = int(a)
    b = int(b)
    c = a * b
    list1.append(c)
# print(list1)
a = list1[0]
b = list1[1]
c = list1[2]

if a > b > c:
    print(a)
elif a > c > b:
    print(a)
elif b > a > c:
    print(b)
elif b > c > a:
    print(b)
elif c > a > b:
    print(c)
elif c > b > a:
    print(c)




