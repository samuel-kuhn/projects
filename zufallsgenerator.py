import time

# time.time_ns is accurate up to 200 nanoseconds so we have to divide by 200
seed = int(time.time_ns()/200)

print(int(time.time_ns()/200) % 10)




