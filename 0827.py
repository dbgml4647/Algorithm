#42 요일 구하기
import datetime
#import time


m = int(input())
d = int(input())

daylist = {
          0 : "MON",
          1 : "TUE",
          2 : "WEN",
          3 : "THU",
          4 : "FRI",
          5 : "SAT",
          6 : "SUN"

}

day = datetime.date(2020,m,d).weekday()
print(daylist[day])