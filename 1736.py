# 초를 입력받아 일 / 시 / 분 / 초의 형태로 나타내시오.

time = int(input())

day = int(time / 86400)
time -= int(86400 * day)

hour = int(time / (60 * 60))
time -= int(3600 * hour)

minute = int(time / 60)
time -= int(60 * minute)

second = int(time)

# print("%d %d %d %d" % day % hour % minute % second)
print(day, hour, minute, second)