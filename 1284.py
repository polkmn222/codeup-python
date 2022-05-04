# 두 소수의 곱을 암호로 사용하는 알고리즘은 큰 수의 소인수분해가 어렵기 때문에 안전하다고 알려져있다.
#
# 그렇지만, 만약 두 소수를 잊어버리면 어떻게 될까? 굉장히 난감할 것이다.
#
# 이에 대비해 어떤 수(n)가 입력되면 두 소수의 곱으로 나타낼 수 있으면 두 소수를 오름차순으로 출력하고,
#
# 그렇지 않으면 "wrong number"를 출력하는 프로그램을 작성하시오.

def prime(n):
    if n == 2:
        return True
    for i in range(2, int(n/2+1)):
        if n % i == 0:
            return False
    return True


n = int(input())
a = 0
b = 0

for j in range(2, n):
    if prime(j):
        if n % j == 0:
            if prime(int(n / j)):
                a = j
                b = int(n / j)
                break
        else:
            continue
if a >= 2:
    print(int(a), int(b))
else:
    print("wrong number")
