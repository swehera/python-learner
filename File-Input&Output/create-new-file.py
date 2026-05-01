import os

# file path
base_path = "D:\\HIRA\\python\\File-Input&Output"

# file name input
createNewFile = input("Enter the file name: ")
file_path = f"{base_path}\\{createNewFile}"

# write content function
def createAndWrite():
    with open(file_path, "w") as new_file:
        new_content = input("Write your content: ")
        new_content = new_content.replace("\\n", "\n")  # newline fix
        new_file.write(new_content)

# read content function
def readContent():
    with open(file_path, "r") as file:
        print("-------- file content ---------")
        print(file.read())

# 🔥 main logic
if os.path.exists(file_path):
    print("File already exists ✅")
    readContent()
else:
    print("File not found ❌ → creating new file...")
    createAndWrite()
    readContent()