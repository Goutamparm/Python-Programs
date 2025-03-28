#Program-1: Reading an Entire File(r mode) python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

#Program-2: Reading Line by Line(r mode) python
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

#Program-3: Writing to a File(Overwrite)(w mode) python
with open("write_example.txt", "w") as file:
    file.write("This is a new line written to the file.")

#Program-4:Writing Multiple Lines to a File(w mode) python
lines = ["First line", "Second line", "Third line"]
with open("write_example.txt", "w") as file:
    for line in lines:
        file.write(line + "\n")

#Program-5:Appending Content to a File(a mode) python
with open("example.txt", "a") as file:
    file.write("\nThis line is appended to the file.")

#Program-6: Reading and Writing in the Same Program(r and w modes) python
with open("example.txt", "r") as read_file:
    content = read_file.read()

with open("copy_example.txt", "w") as write_file:
    write_file.write(content)

#Program-7: Check if File Exists Before Reading(r mode) python
import os

file_path = "example.txt"
if os.path.exists(file_path):
    with open(file_path, "r") as file:
        print(file.read())
else:
    print(f"{file_path} does not exist.")

#Program-8: Write to a File Without Overwriting Existing Content(a mode)
with open("append_example.txt", "a") as file:
    file.write("This line is added to an existing file.\n")

#Program-9: Overwrite Only if File Doesn’t Exist(x mode)
try:
    with open("new_file.txt", "x") as file:
        file.write("This file was created and written to because it did not exist.")
except FileExistsError:
    print("File already exists.")

#Program-10: Reading, Writing, and Appending in Binary Mode(rb, wb, ab)
binary_data = b'\x00\x01\x02\x03'

with open("binary_example.bin", "wb") as file:
    file.write(binary_data)

with open("binary_example.bin", "rb") as file:
    content = file.read()
    print(content)

with open("binary_example.bin", "ab") as file:
    file.write(b'\x04\x05')