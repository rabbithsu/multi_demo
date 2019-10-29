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
                test()
            except Queue.Empty:
                self.log("empty queue.")
                break
            self.log("finish, " + str(q.qsize()) + " remain.")
            q.task_done()
            self.workload += 1
        self.log("Finished task: " + str(self.workload))
        self.log("thread end.")

    def join(self, timeout=None):
        self.log("thread join.")
        self.stop_event.set()
        Thread.join(self, timeout)

    def log(self, message):
        print("Worker %d: %s" % (self.num, message))



def multi_start():
    worker_list =[]
    working_q = Queue.Queue()
    for i in range(0, worker_num):
        worker = worker_thread(working_q, i)

        worker_list.append(worker)


    for i in range(0, 1000):
        working_q.put(str(i))
    for i in worker_list:
        i.start()

    working_q.join()
    for i in worker_list:
        i.join()

    print "\nJobs all dones!"


if __name__ == '__main__':
    start = time.time()
    multi_start()
    time_duration = time.time() - start
    print "Data process: " + str(time_duration) + "s."
