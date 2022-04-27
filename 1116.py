"""
두 정수를 입력받아 아래와 같이 출력하시오.

예)  3 2

3+2=5
3-2=1
3*2=6
3/2=1
"""
a, b = input().split()
a = int(a)
b = int(b)
print('%d'%a,'+%d'%b,'=%d'%(a+b), sep ='')
print('%d'%a,'-%d'%b,'=%d'%(a-b), sep ='')
print('%d'%a,'*%d'%b,'=%d'%(a*b), sep ='')
print('%d'%a,'/%d'%b,'=%d'%(a/b), sep ='')
