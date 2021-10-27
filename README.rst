==================================================
Bounded ThreadPoolExecutor and ProcessPoolExecutor
==================================================

If we use concurrent.futures' ThreadPoolExecutor, ProcessPoolExecutor, easy to run into OOM issue since
their waiting task queue size is not bounded. There is no limit how many tasked submitted.

BoundedThreadPoolExecutor

.. code-block:: python

    from bounded_executor import BoundedThreadPoolExecutor

    def job(i):
        print(i)


    with BoundedThreadPoolExecutor(max_workers=10, max_waiting_tasks=50) as pool:
        for i in range(1000):
            pool.submit(job, i)


BoundedProcessPoolExecutor

.. code-block:: python

    from bounded_executor import BoundedProcessPoolExecutor

    def job(i):
        print(i)


    with BoundedProcessPoolExecutor(max_workers=10, max_waiting_tasks=50) as pool:
        for i in range(1000):
            pool.submit(job, i)