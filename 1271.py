# 입력의 개수 n이 입력되고 n개의  데이터가 입력된다.
#
# 이 n개의 데이터 중 최대값을 출력한다.

a = int(input())
num = list(map(int, input().split()))
arr = num[0]

for i in range(len(num)):
    if num[i] > arr:
        arr = num[i]
print(arr)
