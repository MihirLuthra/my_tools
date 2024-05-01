import multiprocessing
import os
import signal
import sys

def fib(n):
    """Recursively calculates the nth Fibonacci number, a CPU-intensive task."""
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def worker():
    """Function for each worker to run; continuously calculates Fibonacci numbers."""
    while True:
        fib(34)  # Adjust the Fibonacci number for desired CPU load

def stop_processes(signum, frame):
    """Handles clean termination of the program on receiving a SIGINT (Ctrl+C)."""
    print("Interrupt received, stopping processes...")
    sys.exit(0)

def consume_cpu():
    num_cpus = multiprocessing.cpu_count()
    num_cpus = 6
    print(f"Starting {num_cpus} worker processes to maximize CPU load...")
    processes = []

    for _ in range(num_cpus):
        p = multiprocessing.Process(target=worker)
        p.start()
        processes.append(p)

    # Setup clean exit
    signal.signal(signal.SIGINT, stop_processes)
    signal.pause()  # Wait for a signal (like SIGINT)

if __name__ == "__main__":
    consume_cpu()

