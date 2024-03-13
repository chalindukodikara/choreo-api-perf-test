import json
from kind import generate_component_kind
from db import insert_kind, clear_kind_table, insert_data_with_threads, insert_multiple_kind_data_with_threads
from utils import get_input
import time
import os

NUM_OF_THREADS = 24
# NUM_OF_THREADS = os.cpu_count()
# print("Number of threads:", NUM_OF_THREADS)
# if os.cpu_count() == None:
#     NUM_OF_THREADS = 8


def main():
    num_times, clear_table_flag, use_threads_flag, use_multiple_kinds_flag = get_input()

    if clear_table_flag:
        clear_kind_table()

    if use_threads_flag:
        if use_multiple_kinds_flag:
            start_time = time.time()
            insert_multiple_kind_data_with_threads(num_times, NUM_OF_THREADS)
            time_taken = time.time() - start_time
            print(f"{num_times} records inserted successfully in {time_taken:.1f} seconds.", num_times//NUM_OF_THREADS, "records per thread.")
            print(f"{num_times} records inserted successfully in {time_taken/60:.2f} minutes. Number of threads: {NUM_OF_THREADS}")
            return
        start_time = time.time()
        insert_data_with_threads(num_times, NUM_OF_THREADS)
        time_taken = time.time() - start_time
        print(f"{num_times} records inserted successfully in {time_taken:.1f} seconds.", num_times//NUM_OF_THREADS, "records per thread.")
        print(f"{num_times} records inserted successfully in {time_taken/60:.2f} minutes. Number of threads: {NUM_OF_THREADS}")
        return

    start_time = time.time()
    for i in range(num_times):
        component_kind = generate_component_kind()
        # print(json.dumps(component_kind, indent=4))
        insert_kind(component_kind)
    time_taken = time.time() - start_time

    print(f"{num_times} records inserted successfully in {time_taken:.1f} seconds.")
    print(f"{num_times} records inserted successfully in {time_taken/60:.2f} minutes.")


if __name__ == "__main__":
    main()
