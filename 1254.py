"""
시작 알파벳과 마지막 알파벳을 입력받아 그 두 알파벳 사이의 모든 알파벳을 출력하시오.
"""
a,b = input().split()
a = ord(a)
b = ord(b)

#print(a,b)
for i in range(a,b+1):
    print(chr(i),end=" ")
