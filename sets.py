thisset = {"apple", "banana", "cherry", "apple"}
thisset.add("orange")
thisset.remove("banana")
for names in thisset:
    print(names)

print("-----------------")
set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}

set3 = set1.union(set2)

for elements in set3:
    print(elements)

print("-------write empty set, clear set----------")
collection = set()
print(type(collection))
print(thisset)
thisset.clear()# clear the set 
print(len(thisset))

print("---------set methods--------")
setOne = {1,2,3}
setTwo = {3, 4, 5, 6}
setThree = setOne.union(setTwo); #combine both set values and returns new
print(setThree);
setFour = setOne.intersection(setTwo) # combines common values & returns new
print(setFour)



