"""
주민등록번호는 생년월일과 성별정보, 지역정보로 이루어진다.

여기서 생년월일과 성별정보만 입력으로 받겠다.

성별 정보는 1이면 1900년대 출생 남자, 2이면 1900년대 출생 여자, 3이면 2000년대 출생 남자, 4이면 2000년대 출생 여자를 말한다.

기준년도는 2012년도이다. 현재 나이를 출력하시오. 
"""
a, b = input().split()
a = int(a)
b = int(b)
c = int(a / 10000)
c = 1900 + c
# print(c)
d = int(a / 10000)
d = 2000 + d
if b==1 or b==2:
    print(2012-c+1)
else:
    print(2012-d+1)

