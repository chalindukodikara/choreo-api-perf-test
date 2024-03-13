
def get_input():
    num_times = int(input("Enter the number of times to insert data: "))
    clear_table_flag_input = input("Do you want to clear the table before inserting data? (y/n): ").strip().lower()
    use_threads_flag_input = input("Do you want to use threads for inserting data? (y/n): ").strip().lower()
    use_multiple_kinds_flag_input = input("Do you want to use multiple kinds for inserting data? (y/n): ").strip().lower()
    if clear_table_flag_input == 'y':
        clear_table_flag = True
    elif clear_table_flag_input == 'n':
        clear_table_flag = False
    else:
        raise ValueError("Invalid input. Please enter either 'y' or 'n'.")
    
    if use_threads_flag_input == 'y':
        use_threads_flag = True
    elif use_threads_flag_input == 'n':
        use_threads_flag = False
    else:
        raise ValueError("Invalid input. Please enter either 'y' or 'n'.")
    
    if use_multiple_kinds_flag_input == 'y':
        use_multiple_kinds_flag = True
    elif use_multiple_kinds_flag_input == 'n':
        use_multiple_kinds_flag = False
    else:
        raise ValueError("Invalid input. Please enter either 'y' or 'n'.")

    return num_times, clear_table_flag, use_threads_flag, use_multiple_kinds_flag
