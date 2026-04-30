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

print("----------------apna colleage----------")
str = "I am hira"
for char in str:
    if(char=="h"):
        print("h found")
        break
    print(char)

print("END")
print("----------------practice exercise----------")
print("----------------exercise 1----------")
#print the elements of the following list using a loop
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
numbers =  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for elements in numbers:
    print(elements)

print("----------------exercise 2----------")
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = int(input("Enter the finding value: "))
index = 0
for elements in numbers:
    if(elements == x):
        print("Find the value :", elements, ", Index Number: ", index)
        break
    index = index + 1 # for tracking the index
print("Finding Successfull")

print("----------------exercise (sum of array elements)----------------")

# WAP to find the sum of first n numbers using while 
# sum = 1 + 2 + 3 + 4 + 5 
n = int(input("Enter Number: "))
sum = 0
for i in range(1, n+1):
    sum = sum + i
    print(i, "Sum: ", sum)

print("----------------exercise (factorial)----------------")
# WAP to find the factorial of first n numbers. (using for loop)
# factorail = 1 * 2 * 3 * 4 * 5
factoraial = 1
for i in range(1, n + 1):
    factoraial = factoraial * i
    print(i, " factoraial: ", factoraial)

