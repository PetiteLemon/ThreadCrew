import time
import threadcrew
import sleepandprintjob as job


class User:
    def __init__(self):
        self._pool = threadcrew.ThreadCrew(threads=10)
        started = time.time()
        for loop in range(3):
            for _ in range(10):
                self._pool.add(job.SleepAndPrint(1, "a_"+str(loop), self.callback))
                self._pool.add(job.SleepAndPrint(2, "b_"+str(loop), lambda: print("callback lambda")))
                self._pool.add(job.SleepAndPrint(1.5, "c_"+str(loop), lambda: None))

    def callback(self):
        print("callback from main thread")

    def exit(self):
        self._pool.exit(wait_until_queue_empty=True)


u = User()
time.sleep(3)
u.exit()
