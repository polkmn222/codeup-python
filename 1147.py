"""
정수 a, x를 입력받아 a의 값을 x만큼 SHIFT(<<) 연산한 후 결과를 출력하시오.

참고)

비트 이동연산자 << 은 주어진 a를 구성하고 있는 비트를 왼쪽으로 x번 이동한 후 결과를 보여준다.

이러한 비트 연산을 SHIFT 연산이라고도 부르고, <<로 표시한다.
"""
a, b = input().split()
a = int(a)
b = int(b)
print(a<<b)