# 어떤 숫자가 입력되면 그 숫자가 몇 자릿수 숫자인지 알아내는 프로그램을 작성하시오.
import math
a = int(input())
b = int(math.log(a, 10) + 1)
print(b)


