from multiprocessing import Process, Queue, Event
import multiprocessing
import Queue
import time
import sys
import os
import requests

worker_num = 1
if len(sys.argv) == 2:
    worker_num = int(sys.argv[1])

def test():
    a = 0
    while (a < 100000):
        a += 1
        continue

class worker_thread(Process):
    def __init__(self, q, num):
        Process.__init__(self)
        self.q = q
        self.num = num
        self.workload = 0
        #self.s = requests.Session()
        self.stop_event = Event()

    def run(self):
        q = self.q
        while not self.stop_event.is_set():
            try:
                f = q.get(False)
                #download_sample(f, auth_token, destination_directory="samples")
                download_sample(f, auth_token, destination_directory="samples", session=self.s)
            except Queue.Empty:
                self.log("empty queue.")
                break
            self.log("finish job" + str(f) + ", " + str(q.qsize()) + " remain.")
            q.task_done()
            self.workload += 1
        self.log("Finished task: " + str(self.workload))
        self.log("thread end.")

    def join(self, timeout=None):
        self.log("thread join.")
        self.stop_event.set()
        Process.join(self, timeout)

    def log(self, message):
        print("Worker %d: %s" % (self.num, message))



def multi_start(d):
    worker_list =[]
    manager = multiprocessing.Manager()
    working_q = manager.Queue()
    for i in range(0, worker_num):
        worker = worker_thread(working_q, i)
        worker_list.append(worker)

    file_list = [1064946424, 1064946310, 1064748652, 1064693542, 1064571378, 1064571363, 1064440049, 1064308378,
                 1064308363, 1064308341, 1064308281, 1064109830, 1064109795, 1063703843, 1063596666]
    result = []
    for i in file_list:
        working_q.put(i)
    for i in worker_list:
        i.start()

    working_q.join()
    for i in worker_list:
        i.join()

    print "\nJobs all dones!"


def download_sample(key, auth_token, destination_directory=".", file_name=None, session=None, server_ip="172.16.77.46"):
    '''
    Function to download samples to your local host
    :param key: file_id, md5, sha1, or sha256 of the sample
    :param auth_token: your token, as obtained from http://172.16.77.46/usergroup/api_key/
    :param destination_directory: OPTIONAL: destination dir of the downloaded samples
    :param file_name: OPTIONAL: the file name you wish to use for the sample, default is the FileName in ST3
    :param session: OPTIONAL: a requests.Session() object can be passed in for connection reuse
    :param server_ip: OPTIONAL: specify alternate IP for the server, used for server subnet
    :return: the path to the sample if successful, an exception on errors
    '''
    print "test"
    #  If a requests.Session() object is not passed in, just do a normal requests.get
    if not session:
        session = requests

    # Just in case someone feeds the download link from CSV, handle it gracefully and just use the link
    if '/api/sample_download/' in str(key):
        url = key
    else:
        url = "http://{0}/api/sample_download/{1}/".format(server_ip, key)
    headers = {'Authorization': "Token {0}".format(auth_token)}
    num_attempts = 0
    if not os.path.exists(destination_directory):
        os.mkdir(destination_directory)
    if not os.path.isdir(destination_directory):
        raise OSError("Destination directory can not be created, file with that name already exists")
    while True:
        response = session.get(url, headers=headers, stream=True)
        num_attempts += 1
        if response.status_code == 404:
            raise FileNotFoundError("Unable to find a sample with that ID or checksum")
        elif response.status_code == 400:
            raise ValueError("Invalid file ID or checksum as input")
        elif response.status_code == 503:
            #  Too many requests, if too many failures, raise an exception, otherwise, retry
            if num_attempts > 5:
                raise LookupError("Too many requests")
            # escalating backoff
            time.sleep(num_attempts * 2)
        elif response.status_code == 200:
            filename = None
            content_disposition = response.headers.get('content-disposition')
            if content_disposition:
                filename = content_disposition.replace("attachment; filename=", "").replace('"', '')
            if not filename:
                filename = key
            if file_name:
                filename = file_name

            file_destination = os.path.join(destination_directory, str(filename))

            with open(file_destination, 'wb') as of:
                for chunk in response.iter_content(chunk_size=4096):
                    if chunk:
                        of.write(chunk)
            content_length = response.headers.get('content-length')
            if content_length:
                if os.path.getsize(file_destination) != int(content_length):
                    raise IOError("Size of downloaded file does not match")
            # File has successfully downloaded
            return file_destination
        else:
            raise LookupError("Issues with fetching file")


###################
#  Example of use #
###################
file_id = 777777777
md5 = "b23b598a64bf5dc5dd3f7542231b6c4b"
sha1 = "debfbaa1e67060cbee91ab25701da6e70f699cb0"
sha256 = "6cfa3971f5d043c65a74bd6572201a40aabb9ba34c82c1ca870416e39b5f629d"

auth_token = "0895ef70b9a728cfdc175838fede3b09525c0f4b"
'''
download_sample(file_id, auth_token)
download_sample(md5, auth_token)
download_sample(sha1, auth_token)
download_sample(sha256, auth_token, destination_directory="samples")

#  Fetch with connection reuse (faster)
session = requests.Session()
download_sample(sha1, auth_token, destination_directory="samples", session=session)
download_sample(sha256, auth_token, destination_directory="samples", session=session)
'''




if __name__ == '__main__':
    '''session_list = []


    for i in range(0, 10):
        session = requests.Session()
        session_list.append(session)
    for i in range(0, len(session_list)):
        print session_list[i]
        download_sample(file_list[i], auth_token, destination_directory="samples", session=session_list[i])

    exit(0)'''
    start = time.time()
    multi_start(False)
    time_duration = time.time() - start
    print "Data process: " + str(time_duration) + "s."
