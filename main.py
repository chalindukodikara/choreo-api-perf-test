import json
from kind import generate_component_kind
from db import insert_component_kind, clear_kind_table
import time

def get_input():
    num_times = int(input("Enter the number of times to insert data: "))
    clear_table_flag_input = input("Do you want to clear the table before inserting data? (y/n): ").strip().lower()
    if clear_table_flag_input == 'y':
        clear_table_flag = True
    elif clear_table_flag_input == 'n':
        clear_table_flag = False
    else:
        raise ValueError("Invalid input. Please enter either 'y' or 'n'.")
    return num_times, clear_table_flag

def main():
    num_times, clear_table_flag = get_input()

    if clear_table_flag:
        clear_kind_table()

    start_time = time.time()
    for i in range(num_times):
        component_kind = generate_component_kind()
        print(json.dumps(component_kind, indent=4))
        insert_component_kind(component_kind)
    time_taken = time.time() - start_time

    print(f"{num_times} records inserted successfully in {time_taken:.1f} seconds.")
    print(f"{num_times} records inserted successfully in {time_taken/60:.2f} minutes.")


if __name__ == "__main__":
    main()
