import time
import threading

import threadcrew


# part A: implement threadpool to support the following code
def sleepAndPrint(timeToSleep, whatToPrint):
    time.sleep(timeToSleep)
    print(f"{threading.get_ident()}: {whatToPrint}")


threadPool = threadcrew.ThreadCrew(threads = 10)
for _ in range(3):
    for _ in range(10):
        threadPool.add(sleepAndPrint, {"timeToSleep": 2, "whatToPrint": "a" })
    for _ in range(10):
        threadPool.add(sleepAndPrint, {"timeToSleep": 1, "whatToPrint": "b" })
    for _ in range(10):
        threadPool.add(sleepAndPrint, {"timeToSleep": 1.5, "whatToPrint": "c" })

threadPool.waitForFinish()
print("Done... :)")



# part B: edit the threadpool to support classes and not functions
###
# class SleepAndPrint:
#     def __init__(self, timeToSleep, whatToPrint):
#         self._timeToSleep = timeToSleep
#         self._whatToPrint = whatToPrint
#
#     def __call__(self):
#         time.sleep(self._timeToSleep)
#         print(f"{threading.get_ident()}: {self._whatToPrint}")
#
# threadPool.add(SleepAndPrint(2,"a"))
###