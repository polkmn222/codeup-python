"""
1부터 n까지 정수를 계속 더해 나간다고 할 때,
어디까지 더해야 입력한 수보다 같거나 커지는 지를 알아보고자하는 문제이다.
"""

a = int(input())
total = 0

for i in range(1,1000):
    total += int(i)
    if total >= a:
        print(i)
        break
    


"""
while True:
    total += 1
    if total >= a:
        break
print(total)
    
for i in range(1,10):
    print(i)
"""
