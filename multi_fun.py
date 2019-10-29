import threading
import time
import sys
import Queue


def job(num, q):
    print num
    while q > 0:
        a = 0
        while (a < 100000):
            a += 1
            continue
        q -= 1

def job0(num, q):
    print num
    while q > 0:
        a = 0
        while (a < 100000):
            a += 1
            continue
        q -= 1
def job1(num, q):
    print num
    while q > 0:
        a = 0
        while (a < 100000):
            a += 1
            continue
        q -= 1
def job2(num, q):
    print num
    while q > 0:
        a = 0
        while (a < 100000):
            a += 1
            continue
        q -= 1
def job3(num, q):
    print num
    while q > 0:
        a = 0
        while (a < 100000):
            a += 1
            continue
        q -= 1
def job4(num, q):
    print num
    while q > 0:
        a = 0
        while (a < 100000):
            a += 1
            continue
        q -= 1
def job5(num, q):
    print num
    while q > 0:
        a = 0
        while (a < 100000):
            a += 1
            continue
        q -= 1
def job6(num, q):
    print num
    while q > 0:
        a = 0
        while (a < 100000):
            a += 1
            continue
        q -= 1
def job7(num, q):
    print num
    while q > 0:
        a = 0
        while (a < 100000):
            a += 1
            continue
        q -= 1
def job8(num, q):
    print num
    while q > 0:
        a = 0
        while (a < 100000):
            a += 1
            continue
        q -= 1
def job9(num, q):
    print num
    while q > 0:
        a = 0
        while (a < 100000):
            a += 1
            continue
        q -= 1


job_list = [job0, job1, job2, job3, job4, job5, job6, job7, job8, job9 ]

def multi_start(d):
    worker_num = 1
    if len(sys.argv) == 2:
        worker_num = int(sys.argv[1])

    j = 1000 / int(worker_num)
    threads = []
    for i in range(worker_num):
        threads.append(threading.Thread(target = job_list[i], args = (i,j)))
        threads[i].start()


    for i in range(worker_num):
        threads[i].join()

    print("Done.")
if __name__ == '__main__':
    start = time.time()
    multi_start(False)
    time_duration = time.time() - start
    print "Data process: " + str(time_duration) + "s."
