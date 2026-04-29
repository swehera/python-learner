names = ["Hira", "Himel", "Didar", "Shorif"]
relative = ["Nafiz", "Nehal", "Yeana"]

n = len(names) -1
i = 0

while i <= n:
    print(names[i])
    i = i + 1

print('-----------------')
# add item value
names.append("Sanjid");
for name in names:
    print(name);

print('-----------------')

# insert item 
names.insert(0, "Lutfa");
for name in names:
    print(name);

print('-----------------')

# To append elements from another
# list to the current list, 
# use the extend() method.

names.extend(relative);
for name in names:
    print(name);

print('-----------------')

# Remove List Items
names.remove('Sanjid');
for name in names:
    print(name);


student = ["hira", 95.4, "cmt"];
print(student[0:2])

