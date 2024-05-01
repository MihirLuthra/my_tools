import time
import random

def consume_ram():
    large_array = []
    try:
        while True:
            print("Allocating new block")
            # Allocate memory by appending a new block of data
            new_block = ' ' * 10**9  # Approximately 1 GB of data
            large_array.append(new_block)
            print("Allocated {} GB".format(len(large_array)))
            
            time.sleep(1)  # Sleep for 1 second to slow down the process slightly
    except MemoryError:
        print("Memory limit reached")

if __name__ == "__main__":
    consume_ram()

