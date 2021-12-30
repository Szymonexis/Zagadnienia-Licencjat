import os

file_names = ['1-10.md', '11-20.md', '21-30.md', '31-40.md', '41-50.md']

master_file_name = 'master.md'

with open(os.path.join('.', master_file_name), "a", encoding="utf8") as master_file:
    for file_name in file_names:
        with open(os.path.join('.', file_name), "r", encoding="utf8") as file:
            master_file.write(file.read())
            master_file.write("\n\n\n")