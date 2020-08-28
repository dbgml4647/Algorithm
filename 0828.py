#45
import time

print(time.ctime().split(' ')[-1])

time_now = time.time()
time_now = int(time_now / (3600 * 24 * 365))+1970
print(time_now)