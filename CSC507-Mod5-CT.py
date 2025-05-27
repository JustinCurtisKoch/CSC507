# CSC507 Operating Systems Module 5 Critical Thinking
# Evaluate and Experiment With Virtual Memory Settings on a Computer

import time
import os
import psutil

# Start timer
start_time = time.time()

# Get total virtual memory
virtual_mem = psutil.virtual_memory().total / (1024 ** 3)  # in GiB

# Print current virtual memory setting
print(f"Virtual Memory (RAM + Pagefile): {virtual_mem:.2f} GiB")

# Build a large list to stress memory
stress_list = []
for i in range(1, 100000):
    stress_list.append(str(i) * 100) # Create a large string to consume memory

# End timer
end_time = time.time()
execution_time = end_time - start_time

# Write result to log file
with open("test_results_log.txt", "a") as log_file:
    log_file.write(f"Virtual Memory: {virtual_mem:.2f} GiB | Time to complete: {execution_time:.4f} seconds\n")

print(f"Script completed in {execution_time:.4f} seconds.")
