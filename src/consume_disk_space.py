import os
import signal
import time

# Directory to store temporary files
temp_dir = "temp_storage"
os.makedirs(temp_dir, exist_ok=True)

# Function to handle clean up on interruption
def clean_up(signum, frame):
    print("Interrupt received, cleaning up...")
    for filename in os.listdir(temp_dir):
        file_path = os.path.join(temp_dir, filename)
        os.remove(file_path)
        print(f"Deleted {file_path}")
    os.rmdir(temp_dir)
    print("Cleanup complete. Exiting.")
    exit(0)

# Register the signal handler for clean-up on Ctrl+C
signal.signal(signal.SIGINT, clean_up)

def consume_disk_space():
    file_index = 0
    try:
        while True:
            file_path = os.path.join(temp_dir, f"temp_file_{file_index}.bin")
            # Write approximately 1 GB to the file
            with open(file_path, 'wb') as f:
                f.write(b'\0' * 10**10)  # Writing null bytes to create a file of about 1 GB
            print(f"Created {file_path}")
            file_index += 1
            time.sleep(1)  # Sleep to slow down file creation and observe the process
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    consume_disk_space()

