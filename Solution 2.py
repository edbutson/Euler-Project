__author__ = 'Eric and Lynse'
import time
t0 = time.time()
ans = 0
i = 0
j = 1
l = 0
while l <= 4000000:
    l = i + j
    if l%2 == 0:
        ans += l
    i = j
    j = l
t1 = time.time()
print(ans)
print(t1-t0)
