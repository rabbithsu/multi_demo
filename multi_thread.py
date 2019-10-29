import re
import os
import sys


from threading import Timer, Thread, Event

import Queue

import time

worker_num = 1
if len(sys.argv) == 2:
    worker_num = int(sys.argv[1])
def test():
    a = 0
    while (a < 100000):
        a += 1
        continue
        # print "Noooooooooooooooo"
def test0():
    a = 0
    while (a < 100000):
        a += 1
        print str(a)
        continue
        # print "Noooooooooooooooo"
def test1():
    a = 0
    while (a < 100000):
        a += 1
        continue
def test2():
    a = 0
    while (a < 100000):
        a += 1
        continue
def test3():
    a = 0
    while (a < 100000):
        a += 1
        continue
def test4():
    a = 0
    while (a < 100000):
        a += 1
        continue
def test5():
    a = 0
    while (a < 100000):
        a += 1
        continue
def test6():
    a = 0
    while (a < 100000):
        a += 1
        continue
def test7():
    a = 0
    while (a < 100000):
        a += 1
        continue
def test8():
    a = 0
    while (a < 100000):
        a += 1
        continue
def test9():
    a = 0
    while (a < 100000):
        a += 1
        continue

worker_fun = [test0, test1, test2, test3, test4, test5, test6, test7, test8, test9]


class worker_thread(Thread):
    def __init__(self, q, num):
        Thread.__init__(self)
        self.q = q
        self.num = num
        self.workload = 0
        self.stop_event = Event()

    def run(self):
        q = self.q
        while not self.stop_event.is_set():
            try:
                f = q.get(False)
                worker_fun[int(self.num)]
            except Queue.Empty:
                self.log("empty queue.")
                break
            self.log(f + " is done.")
            self.log("finish, " + str(q.qsize()))
            q.task_done()
            self.workload += 1
            self.log("task done, " + str(q.qsize()))
        self.log("thread end.")

    def join(self, timeout=None):
        self.log("thread join.")
        self.log("Finished task: " + str(self.workload))
        self.stop_event.set()
        Thread.join(self, timeout)

    def log(self, message):
        print("Worker %d: %s" % (self.num, message))



def multi_start(d):
    worker_list =[]
    #manager = multiprocessing.Manager()
    working_q = Queue.Queue()
    for i in range(0, worker_num):
        worker = worker_thread(working_q, i)

        worker_list.append(worker)
        # print "Worker " + str(i) + "is set!"


    result = []
    for i in range(0, 1000):
        working_q.put(str(i))
    for i in worker_list:
        i.start()
    print "end delivery list."
    working_q.join()
    for i in worker_list:
        i.join()

    print result
    print "lenth: " + str(len(result))



if __name__ == '__main__':
    start = time.time()
    multi_start(False)
    time_duration = time.time() - start
    print "Data process: " + str(time_duration) + "s."
