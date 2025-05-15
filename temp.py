#file = open("ticket.txt", "w")
#with open("ticket.txt", "r") as file:
 #   print(int(file.read()) + 1)
#file.close()
import datetime

now = datetime.datetime.now()
print(now)
print(f"현재 시각 : {now.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"현재 시각 : {now.strftime('%Y년 %m월 %d일 %H시 %M분 %S초')}")