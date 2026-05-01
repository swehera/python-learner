count = 0

with open("D:\\HIRA\\python\\File-Input&Output\\numbers.txt", "r") as file:
    data = file.read()

    nums = data.split(",")
    for value in nums:
        if(int(value) % 2 == 0):
            print(int(value))
            count += 1

# print(count)