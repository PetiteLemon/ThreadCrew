import threading
import time

import job


class SleepAndPrint(job.Job):
    def __init__(self, timeToSleep, whatToPrint, callback):
        self._timeToSleep = timeToSleep
        self._whatToPrint = whatToPrint
        self._callback = callback

    def run(self):
        time.sleep(self._timeToSleep)
        print(f"{threading.get_ident()}: {self._whatToPrint}")

    def callback(self):
        self._callback()
