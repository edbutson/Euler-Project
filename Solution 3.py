import time
var = 600851475143
small = int(var **0.5)
factors = []
chk = []
lst = range(small+1)
start = time.time()
for i in lst[::-1]:
    if var % i == 0:
        for j in range(2,i):
            if i%j == 0:
                chk.append(j)
        if len(chk) == 0:
            print(i)
            break
        chk = []
end = time.time()
print(end - start)
