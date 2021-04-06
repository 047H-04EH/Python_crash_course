#access elements in a list by index [0]
bicycles=['trek','cannondale','redline','specialized']
print(bicycles[0])

#capitalizes the first item at a certain index
print(bicycles[0].title())

#using values from a list by index in a message
message="My first bicycle was a "+bicycles[0].title()+ "."
print(message)

#modify an element in a list by index
motorcycles=['honda','yamaha', 'suzuki']
print(motorcycles)

#chances the element honda to ducati
motorcycles[0]='ducati'
print(motorcycles)

#add an element to the end of a list
motorcycles.append('ducati')
print(motorcycles)

#inserting an element into a list at a certain index
motorcycles=['honda','yamaha','suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles)

#remove an item from a list using del
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

#removing items using the pop() method
#suzuki was removed from the end of the list and is
#stored in popped_motorcycle
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

popped_motorcycle=motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

#removing an item by value
motorcycles=['honda','yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

#organizing a list permanently with sort()
cars=['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

#temporarily organizing a list with sorted()
cars=['bmw','audi','toyota','subaru']

print("Here is the original list: ")
print(cars)

print("\nHere is the sorted list: ")
print(sorted(cars))

print("\nHere is the original list again: ")
print(cars)

#printing a list in reverse order
#does not reverse alphabetically
cars=['bmw','audi','toyota','subaru']
print(cars)

cars.reverse()
print(cars)

#finding the length of a list
cars=['bmw','audi','toyota','subaru']
len(cars)
print(len(cars))
