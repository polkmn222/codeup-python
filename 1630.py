# 광곽이는 만우절을 맞이하여 아침에 일어나는 학생들을 위해 모든 기상곡 사이에 “AMOLED”를 집어넣으려 한다.
#
# (단, 마지막에는 AMOLED가 오지 않게 한다. 학생들이 싫어한다.)

a = int(input())
# b = list(map(str, input().split()))
b = []
# print(a)
for i in range(a):
    b.append(input())

# print(b)

# for i in range(len(b)):
#     print(b[i])
#     if i % 2 != 0:
#         print("AMOLED")
#     elif i == len(b):
#         break
for i in range(len(b)):
    print(b[i])
    if i == len(b)-1:
        break
    else:
        print("AMOLED")

