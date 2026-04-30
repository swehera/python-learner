n = int(input("Enter Recursion Number: " ))

# recursive function
def show(n):
    if(n == 0): # base case -> for stop the loop 
        return 
    print(n)
    show(n-1) # call himself
    print("End")

# call the recursive function 
show(n)

print("-----------factorial recursive function-----------")
n = int(input("Enter the factorial number: "))
def factrorial(n):
    if(n == 0 or n == 1):
        return 1
    else:
        # print(n)
        return  factrorial(n - 1) * n
    

print("5! =",factrorial(n))

print("-----------exercise 1-----------")
# write a recursice function to calculate the sum of first
# n natural numbers
n = int(input("Write natural number 1 to :"))

def addNaturalNumber(n):
    if(n == 0 ):
        return 0
    else:
        # print(n)
        return addNaturalNumber(n - 1) + n

print(addNaturalNumber(n))
print("-----------exercise 2-----------")
# Write a recursive function to print all elements in a list
# Hint: use list & index as parameters
nameList = ["Hira", "Himel", "Didar", "Shorif"]
i = 0
def traverseRecursive(list, i):
    if(i >= len(nameList)):
        return
    else:
        print(list[i])
        return traverseRecursive(list, i+1)

traverseRecursive(nameList, i)