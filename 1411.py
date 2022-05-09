# 우리는 1부터 N까지의 숫자가 차례대로 적힌 N장의 카드 묶음을 가지고 있다.
# 그런 데 이 카드 묶음을 옮기는 중 실수로 땅에 떨어뜨려 그 중 한 장을 잃어버렸다.
# 여러 분은 땅에 떨어진 카드 묶음을 읽어서 빠진 하나의 카드 번호를 찾아 출력해야 한다.

a = int(input())
# b = list(map(int, input().split()))
b = []
c = []
d = 0
e = 0

for i in range(1, a):
    a1 = int(input())
    # b.append(i)
    e += a1


for i in range(1, a+1):
    c.append(i)
d = sum(c)
# print(c)

# for i in range(1, b+1):
#     e += b[i]

# print(d, e)
print(d-e)