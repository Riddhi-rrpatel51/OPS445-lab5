#!/usr/bin/env python3
# Author ID: rrpatel51

def read_file_string(file_name):
    # Takes file_name as a string for a file name, returns its entire contents as a string
    with open(file_name, 'r') as file:
        return file.read()  # Return the entire file content as a string

def read_file_list(file_name):
    # Takes a file_name as a string for a file name, returns its entire contents as a list of lines
    # Remove the new-line characters
    with open(file_name, 'r') as file:
        return [line.strip() for line in file.readlines()]  # Strip new-line characters and return as list

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))  # Print the entire content as a string
    print(read_file_list(file_name))  # Print the file contents as a list of lines

# Function to append a string to the end of a file
def append_file_string(file_name, string_of_lines):
    with open(file_name, 'a') as file:
        file.write(string_of_lines)

# Function to write a list to a file, each item on a new line
def write_file_list(file_name, list_of_lines):
    with open(file_name, 'w') as file:
        for line in list_of_lines:
            file.write(line + '\n')

# Function to copy data from one file to another with line numbers
def copy_file_add_line_numbers(file_name_read, file_name_write):
    with open(file_name_read, 'r') as read_file:
        with open(file_name_write, 'w') as write_file:
            for index, line in enumerate(read_file, start=1):
                write_file.write(f"{index}:{line}")


# Main block for testing the functions
if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']

    append_file_string(file1, string1)
    print(read_file_string(file1))

    write_file_list(file2, list1)
    print(read_file_string(file2))

    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))
