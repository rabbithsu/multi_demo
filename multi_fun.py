import threading
import time
import sys

def multi_start(d):
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
if __name__ == '__main__':
    start = time.time()
    multi_start(False)
    time_duration = time.time() - start
    print "Data process: " + str(time_duration) + "s."