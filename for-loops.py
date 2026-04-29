names = ["Hira", "Himel", "Didar", "Shorif", "Alamin"]
newlist = []

for item in names:
    print(item)

print('-----------------')

for i in range(len(names)):
    print(names[i])

print('-----------------')

for x in names:
    if "a" in x:
        newlist.append(x)
print(newlist)

print('-----------------')
# sorting and sort dessending
names.sort();
for item in names:
    print(item)
print('-----------------')
names.sort(reverse=True)
for item in names:
    print(item)