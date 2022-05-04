# gbs라는 개미 투자자가 주식에 투자하려고 합니다.
#
# 이 사람이 투자한 돈의 액수와, 그 주식의 하루간의 변동을 퍼센트로 알 때, 이 사람의 순수익과 이득/손해 판단을 출력하세요.
# 첫째줄에 투자한 액수 a가 입력됩니다. (100 <= a <= 10,000)
#
# 둘째 줄에 투자 일 수 b가 입력됩니다.(1 <= b <= 10)
#
# 그 다음줄에 일별 변동폭인 데이터가 날짜 갯수(b개)만큼 퍼센트 정수로 입력됩니다. (변동폭는 음수도 될 수 있습니다.) ( 범위 -100 ~ +100)

a = int(input())
b = int(input())
num = list(map(int, input().split()))
total = a
for i in range(len(num)):
    total += total * (num[i]/100)
benefit = total-a

print(round(benefit))
if benefit>0:
    print("good")
elif benefit<0:
    print("bad")
else:
    print("same")

