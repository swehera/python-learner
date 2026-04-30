seq = range(5) # 0 to 4
print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])
print(seq[4])

# syntax
# range(start?, stop, step)
#--> Range function return a
# sequence of numbers, starting
# from 0 by default, and increments 
# by 1(by default), 
# and stops before a specified number

for i in range(10): # range(stop)
    print(i)

print("---------")

for i in range(1, 5): # range(start, stop)
    print(i)

print("---------")
for i in range(2, 10, 2): # range(start, stop, step)
    print(i)

print("---------")
# 100 to 1
for i in range(100, 0, -1):
    print(i)

print("---------")
# Print the multiplication table of a number n
n = int(input("Enter the number: "))

for i in range(1, 11):
    print(i * n)


print("---------")
for i in range(10):
    pass # empty but still exist for future work

print("Useful working code ")
