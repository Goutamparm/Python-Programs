#Program-1: Write to a Text File
with open("example.txt", "w") as file:
    file.write("Hello, welcome to file handling in Python!")

#Program-2: Read from a Text File
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

#Program-3: Append Text to an Existing File
with open("example.txt", "a") as file:
    file.write("\nLet's append more text!")

#Program-4: Write Multiple Lines to a Text File
lines = ["First line", "Second line", "Third line"]
with open("multiline.txt", "w") as file:
    file.write("\n".join(lines))

#Program-5: Read a File Line by Line
with open("multiline.txt", "r") as file:
    for line in file:
        print(line.strip())

#Program-6: Read and Write Binary Files
data = bytes([100, 120, 130, 150])
with open("binaryfile.bin", "wb") as file:
    file.write(data)

with open("binaryfile.bin", "rb") as file:
    binary_content = file.read()
    print(binary_content)

#Program-7: Copy Contents from One File to Another (Text)
with open("example.txt", "r") as src_file, open("copy_example.txt", "w") as dest_file:
    dest_file.write(src_file.read())

#Program-8: Copy Contents from One File to Another (Binary)
with open("binaryfile.bin", "rb") as src_file, open("copy_binaryfile.bin", "wb") as dest_file:
    dest_file.write(src_file.read())

#Program-9: Read Specific Number of Characters from a File
with open("example.txt", "r") as file:
    content = file.read(10)
    print(content)

#Program-10: Read and Write JSON Data to a File (Text)
import json
data = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

with open("data.json", "w") as file:
    json.dump(data, file)

with open("data.json", "r") as file:
    content = json.load(file)
    print(content)