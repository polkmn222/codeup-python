"""
hello를 20번 연속출력한 다음 한 칸을 띄우고(공백 한칸(줄바꿈 아님)) world를 연속 30번 출력하시오.

"""
for i in range(20):
    print("hello", end ='')

print(" ", end = '')

for i in range(30):
    print("world", end ='')
