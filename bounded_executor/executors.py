from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from queue import Queue
from threading import BoundedSemaphore


class _BoundedThreadPoolExecutor(ThreadPoolExecutor):
    def __init__(self, max_workers, max_waiting_tasks, *args, **kwargs):
        super().__init__(max_workers=max_workers, *args, **kwargs)
        self._work_queue = Queue(maxsize=max_waiting_tasks)


class _BoundedProcessPoolExecutor(ProcessPoolExecutor):
    def __init__(self, max_workers = None, max_waiting_tasks = 0, *args, **kwargs):
        super().__init__(max_workers=max_workers, *args, **kwargs)
        self.semaphore = BoundedSemaphore(self._max_workers + max_waiting_tasks)

    def submit(self, fn, *args, **kwargs):
        self.semaphore.acquire()
        try:
            future = super().submit(fn, *args, **kwargs)
        except:
            self.semaphore.release()
            raise
        else:
            future.add_done_callback(lambda x: self.semaphore.release())
            return future