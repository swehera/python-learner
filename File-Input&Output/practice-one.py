"""
Create a new file "practice.txt" using python. Add the
following data in it:
Hi, Everyone
we are learning File I/O
using Java.
I like programming in Java
"""
"""
Search if the word "learning" exists in the file or not
"""
import os

# file path
base_path = "D:\\HIRA\\python\\File-Input&Output"

# create file
createNewFile = input("Enter the file name: ")
file_path = f"{base_path}\\{createNewFile}"

# write content
with open(file_path, "w") as new_file:
    new_content = input("Write your content: ")
    new_content = new_content.replace("\\n", "\n")  # newline fix
    new_content = new_content.replace("Java", "Python")  # replace example
    new_file.write(new_content)

# read + show content
with open(file_path, "r") as new_file:
    lines = new_file.readlines()

print("\n--------- new content ----------")
print("".join(lines))

# search word + line number
word = input("\nWrite the finding word: ")
found = False

for line_number, line in enumerate(lines, start=1):
    if word.lower() in line.lower():  # case-insensitive search
        print(f"Found in line {line_number}: {line.strip()}")
        found = True

if not found:
    print(f"Not Found the word '{word}'")

# delete file
command_to_delete_file = input("\nDelete New File (yes/no): ")

if command_to_delete_file.lower() == "yes":
    if os.path.exists(file_path):
        os.remove(file_path)
        print("Deleted file successfully")
    else:
        print("File not found")
elif command_to_delete_file.lower() == "no":
    print("File is safe 🙂")
else:
    print("Invalid input")