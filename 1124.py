"""
화학 숙제를 하던 광곽이는 분자량을 구하라는 문제를 보고 귀찮아 한다.

귀찮은 광곽이를 위해서 화학식을 입력하면 분자량을 구해주는 프로그램을 만들어 주자!

화학식은 CxHy의 꼴로 입력된다.

C의 원자량은 12, H의 원자량은 1로 한다.
"""
from sys import stdin

a, b = map(int, stdin.readline()[1:].split('H'))
c = 12 * a + b
print(c)
