import threading
import time
import sys

worker_num = 1
if len(sys.argv) == 2:
    worker_num = int(sys.argv[1])

def job(num):
    print num
    a = 0
    while (a < 100000):
        a += 1
        continue

threads = []
for i in range(worker_num):
    threads.append(threading.Thread(target = job, args = (i,)))
    threads[i].start()


for i in range(5):
    threads[i].join()

print("Done.")