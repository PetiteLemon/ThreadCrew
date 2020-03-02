import threading
import queue


class ThreadCrew:
    def __init__(self, threads):
        assert 0 < threads <= 100, "pool size is between 1 to 100"
        self.queue = queue.Queue()

        self.running = threading.Event()
        self.running.set()
        self._threads = []

        for _ in range(threads):
            t = threading.Thread(target=worker, args=[self.queue, self.running], daemon=True)
            t.start()
            self._threads.append(t)

    def add(self, job):
        self.queue.put(job)

    def exit(self, wait_until_queue_empty=True):
        if wait_until_queue_empty:
            self.queue.join()
        print(f"exiting with empty queue(?): {self.queue.empty()}")

        self.running.clear()
        for t in self._threads:
            t.join()
        print(f"all threads in threadpool terminated")


def worker(jobs_queue, running):
    print(f"thread {threading.get_ident()} Starting")
    counter = 0
    while running.is_set():
        try:
            job = jobs_queue.get(timeout=1)
            counter += 1
            job.run()
            job.callback()
            jobs_queue.task_done()
        except queue.Empty:
            pass
    print(f"thread {threading.get_ident()} Exiting, handled {counter}")
