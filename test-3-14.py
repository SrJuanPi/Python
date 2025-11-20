import time
import threading
import sys

def cpu_bound_task(n):
    count = 0
    for i in range(n):
        count += i * i
    return count

def run_threads(n_threads=8, work_per_thread=10_000_000):
    threads = []
    start = time.perf_counter()

    for _ in range(n_threads):
        t = threading.Thread(target=cpu_bound_task, args=(work_per_thread,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end = time.perf_counter()
    return end - start

if __name__ == "__main__":
    print(f"Python version: {sys.version}")
    print(f"GIL enabled: {sys._is_gil_enabled()}")
    print("Running CPU-bound threading benchmark...")

    duration = run_threads()
    print(f"Execution time: {duration:.2f} seconds")
