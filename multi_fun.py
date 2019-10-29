import threading
import time
import sys
import Queue


def job(num, q):
    print num
    while True:
        try:
            f = q.get(False)
            a = 0
            while (a < 100000):
                a += 1
                continue
            q.task_done()
        except Queue.Empty:
            print("empty queue.")
            break

def job0(num, q):
    print num
    while True:
        try:
            f = q.get(False)
            a = 0
            while (a < 100000):
                a += 1
                continue
            q.task_done()
        except Queue.Empty:
            print("empty queue.")
            break
def job1(num, q):
    print num
    while True:
        try:
            f = q.get(False)
            a = 0
            while (a < 100000):
                a += 1
                continue
            q.task_done()
        except Queue.Empty:
            print("empty queue.")
            break
def job2(num, q):
    print num
    while True:
        try:
            f = q.get(False)
            a = 0
            while (a < 100000):
                a += 1
                continue
            q.task_done()
        except Queue.Empty:
            print("empty queue.")
            break
def job3(num, q):
    print num
    while True:
        try:
            f = q.get(False)
            a = 0
            while (a < 100000):
                a += 1
                continue
            q.task_done()
        except Queue.Empty:
            print("empty queue.")
            break
def job4(num, q):
    print num
    while True:
        try:
            f = q.get(False)
            a = 0
            while (a < 100000):
                a += 1
                continue
            q.task_done()
        except Queue.Empty:
            print("empty queue.")
            break
def job5(num, q):
    print num
    while True:
        try:
            f = q.get(False)
            a = 0
            while (a < 100000):
                a += 1
                continue
            q.task_done()
        except Queue.Empty:
            print("empty queue.")
            break
def job6(num, q):
    print num
    while True:
        try:
            f = q.get(False)
            a = 0
            while (a < 100000):
                a += 1
                continue
            q.task_done()
        except Queue.Empty:
            print("empty queue.")
            break
def job7(num, q):
    print num
    while True:
        try:
            f = q.get(False)
            a = 0
            while (a < 100000):
                a += 1
                continue
            q.task_done()
        except Queue.Empty:
            print("empty queue.")
            break
def job8(num, q):
    print num
    while True:
        try:
            f = q.get(False)
            a = 0
            while (a < 100000):
                a += 1
                continue
            q.task_done()
        except Queue.Empty:
            print("empty queue.")
            break
def job9(num, q):
    print num
    while True:
        try:
            f = q.get(False)
            a = 0
            while (a < 100000):
                a += 1
                continue
            q.task_done()
        except Queue.Empty:
            print("empty queue.")
            break

job_list = [job0, job1, job2, job3, job4, job5, job6, job7, job8, job9 ]

def multi_start(d):
    worker_num = 1
    if len(sys.argv) == 2:
        worker_num = int(sys.argv[1])

    working_q = Queue.Queue()
    for i in range(0, 1000):
        working_q.put(str(i))
    threads = []
    for i in range(worker_num):
        threads.append(threading.Thread(target = job_list[i](), args = (i,working_q)))
        threads[i].start()


    for i in range(worker_num):
        threads[i].join()

    print("Done.")
if __name__ == '__main__':
    start = time.time()
    multi_start(False)
    time_duration = time.time() - start
    print "Data process: " + str(time_duration) + "s."