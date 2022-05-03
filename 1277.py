# 첫 줄에 데이터의 개수 N(N은 홀수)이 입력되고, 그 다음 줄에 N개의 데이터가 입력된다.
#
# 여기서 첫번째 데이터, 중간 데이터, 마지막 데이터를 출력하시오.
a = int(input())
num = list(map(int, input().split()))
b = 0
c = 0
#for i in range(len(num)):
    # print(num[0], num[int(i/2)], num[i-1])
b = num[int(a/2)]
c = num[a-1]
a = num[0]
print(a, b, c)