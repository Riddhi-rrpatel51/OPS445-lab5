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
