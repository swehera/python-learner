
n = int(input("Multiplication Table Number: "))
i = 1
while i <= 10:
    print(i*n)    
    i += 1

print("----------------exercise 2----------------")
# ex2: print the elements of the following list using a loop:
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 10]
i = 1
while i <= 10:
    print(i*i)
    i += 1
print("----------------exercise 3----------------")
print("----------------break----------------")
# Search for a number x in this tuple using loop:
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 10]
numbers = (1, 4, 9, 16, 25, 36, 49, 64, 81, 10)
searchValue = int(input("Enter the searching value: "))
i = 0;
while(i <= len(numbers)-1):
    if(numbers[i]==searchValue):
        print("Index Number: ", i, " value is : ", numbers[i])
        break
    else:
        print("finding...")
    i += 1


print("----------------continue----------------")
print("----------------all odd numbers----------------")
i = 1
while( i <= 10 ):
    if(i % 2 == 0): # print all odd numbers
        i += 1
        continue #skip
    print(i)
    i += 1
print("----------------all even numbers----------------")
i = 1
while( i <= 10 ):
    if(i % 2 != 0): # print all even numbers
        i += 1
        continue #skip
    print(i)
    i += 1


print("----------------exercise----------------")

# WAP to find the sum of first n numbers using while 
# 1 + 2 + 3 + 4 + 5
n = int(input("Enter Number: " ))
i = 1
sum = 0
while(i <= n):
    sum = sum + i
    print(i, "Sum: ", sum)
    i += 1
print("Sum: ", sum)