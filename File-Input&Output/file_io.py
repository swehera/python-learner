import os


# create new file 
createNewFile = input("Enter file Name: ")

with open(f"D:\\HIRA\\python\\File-Input&Output\\{createNewFile}", "w") as file:
    content = input("Write your content: ")
    file.write(content)

with open(f"D:\\HIRA\\python\\File-Input&Output\\{createNewFile}") as file:
    print("-------- new content ---------")
    print(file.read())

# delete the file 
command_to_delete_file = str(input("Delete New File(yes/no): "))
if(command_to_delete_file == "yes"):
    os.remove(f"D:\\HIRA\\python\\File-Input&Output\\{createNewFile}")
    print("Deleted file successfully")
elif(command_to_delete_file == "no"):
    print("File is ok")
else:
    print("----------------------")
