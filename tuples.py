thistuple = ("apple", "banana", "cherry", "apple", "cherry")
# print(len(thistuple))
for names in thistuple:
    print(names)

print(type(thistuple))

print('------------')
y = list(thistuple)
y.append("kola")
thistuple = tuple(y)
for names in thistuple:
    print(names)

print('------------')

fruits = ("apple", "banana", "cherry");
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

print('------------')

tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3);
tuple3 = tuple1 + tuple2

for elements in tuple3:
    print(elements)

print('------------')
# Multiply Tuples
tuple4 = tuple3 * 2
for elements in tuple4:
    print(elements)

