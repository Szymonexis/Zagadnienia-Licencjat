import os
import sys

file_names = ['1-10.md', '11-20.md', '21-30.md', '31-40.md', '41-50.md']

master_file_name = 'master.md'

master_file_path = os.path.join('.', master_file_name)

if os.path.exists(master_file_path) and os.path.isfile(master_file_path):
    sys.path.remove(master_file_path)

with open(os.path.join('.', master_file_name), "a", encoding="utf8") as master_file:
    for file_name in file_names:
        with open(os.path.join('.', file_name), "r", encoding="utf8") as file:
            master_file.write(file.read() + "\n\n")