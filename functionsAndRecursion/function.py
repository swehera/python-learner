def sum(a, b):
    sum = a + b
    return sum

#greetings function
def gretting(name):
    print("Welcome, ",name)

# call the function 
print(sum(100, 200)) # 300
print(sum(55, 87)) # 142

name = str(input("Enter your name: "))
gretting(name)

print("--------------")
# WAF to print the length of a list. (list is the parameter)
names = ["Hira", "Himel", "Didar", "Shorif"]

def listLenth(listdata):
    print(len(listdata))
    return len(listdata)

listLenth(names)
print("--------------")
# WAF to print the elements 
# of a list in a single 
# line (list is the parameter)
def elementsName(listItem):
    for elements in listItem:
        print(elements, end=" ")

elementsName(names)

print()

print("---------------")
# WAF to find the facrorial of n.(n is the parameter)

n = int(input("Enter the factorial number: "))
def findFactorial(n):
    i = 1
    factoral = 1
    while i <= n:
        factoral = factoral * i
        print(i,factoral)
        i += 1
findFactorial(n)
print("---------------")
# WAF to convert USD to BDT
def usdToBdt(amount):
    return amount * 122.74

amount = float(input("Enter the USD amount: "))
print(usdToBdt(amount), "Bangladeshi Taka")