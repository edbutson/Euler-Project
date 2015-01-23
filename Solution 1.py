__author__ = 'Eric and Lynse'
import time
ans = 0
t0 = time.time()
for i in range(1,1000):
    if i%3 == 0 or i%5 == 0 and i%15 != 0:
        ans += i
t1 = time.time()
print(ans)
print(t1-t0)