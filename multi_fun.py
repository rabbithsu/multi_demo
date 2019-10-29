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



def multi_start(d):
    worker_num = 1
    if len(sys.argv) == 2:
        worker_num = int(sys.argv[1])

    working_q = Queue.Queue()
    for i in range(0, 1000):
        working_q.put(str(i))
    threads = []
    for i in range(worker_num):
        threads.append(threading.Thread(target = job, args = (i,q)))
        threads[i].start()


    for i in range(worker_num):
        threads[i].join()

    print("Done.")
if __name__ == '__main__':
    start = time.time()
    multi_start(False)
    time_duration = time.time() - start
    print "Data process: " + str(time_duration) + "s."