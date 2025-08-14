#!/usr/bin/env python3
"""
Author: Sagiran Suresh (ssuresh14)
"""

import getpass
import sys

def user_get():
    # Lab 3 uses: getpass.getuser()
    return getpass.getuser()

def file_op(filename):
    # Modified: print error and halt if file cannot be opened
    try:
        with open(filename, 'r') as f:
            return f.read()
    except Exception:
        print("Error: could not open file")
        sys.exit(1)

def main():
    # Step 3: Call user_get and print welcome message
    user = user_get()
    print(f"Welcome {user}!")

    # Find the text file in the same directory as Final Test.py
    filename = "testfile.txt"  

    # Call file_op and get file content
    content = file_op(filename)

    # Convert file content to list of lines with no newline characters
    pineapple = [line.strip() for line in content.splitlines()]

    # Any item of pineapple which contains a number as the last character should be added to has_num
    has_num = []
    for item in pineapple:
        if item and item[-1].isdigit():
            has_num.append(item)
    # lab4e.py is the lab file where we searched for non-numeric characters

    print("pineapple:", pineapple)
    print("has_num:", has_num)

if __name__ == "__main__":
    main()
