#Program-1: File Not Found Error (FileNotFoundError)
try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found.")

#Program-2: Permission Denied Error (PermissionError)
try:
    with open("/restricted_access_file.txt", "w") as file:
        file.write("Trying to write to a restricted file.")
except PermissionError:
    print("Error: You don't have permission to write to this file.")

#Program-3: Handle General I/O Errors (IOError)
try:
    with open("some_file.txt", "r") as file:
        content = file.read()
except IOError as e:
    print(f"An I/O error occurred: {e}")

#Program-4: Using finally Block for Cleanup
try:
    file = open("sample.txt", "w")
    file.write("Writing to the file.")
except IOError:
    print("An I/O error occurred.")
finally:
    file.close()
    print("File closed successfully.")

#Program-5: Creating a File if It Doesn’t Exist (Avoiding FileNotFoundError)
try:
    with open("new_file.txt", "x") as file:
        file.write("This file has been created.")
except FileExistsError:
    print("File already exists.")

#Program-6: Checking for Errors in File Mode (ValueError)
try:
    mode = "invalid_mode"
    with open("file.txt", mode) as file:
        file.write("This will cause a ValueError.")
except ValueError:
    print("Error: Invalid file mode.")

#Program-7: Handling Errors in File Read and Write Operations
try:
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)
    with open("example.txt", "a") as file:
        file.write("Appending this line.")
except Exception as e:
    print(f"An error occurred: {e}")

#Program-8: Using except with else
try:
    with open("example.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")
else:
    print("File content read successfully.")

#Program-9: Handling Errors in Binary File Operations
try:
    with open("binary_file.bin", "rb") as file:
        data = file.read()
except FileNotFoundError:
    print("Error: Binary file not found.")
except IOError as e:
    print(f"An I/O error occurred: {e}")

#Program-10: Using Custom Error Messages for File Operations
try:
    with open("log.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: The file 'log.txt' does not exist. Please check the file path.")
except PermissionError:
    print("Error: Access denied. Ensure you have the correct permissions.")
except IOError as e:
    print(f"An unexpected I/O error occurred: {e}")