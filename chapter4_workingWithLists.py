#loop through and print all items in a list
magicians=['alice','david','carolina']
for magician in magicians:
    print(magician)

#making a numerical list with the range() function
#does not include 5 in output
for value in range(1,5):
    print(value)

#using range() to make a list of numbers
numbers=list(range(1,6))
print(numbers)

#skip numbers in a given range
even_numbers=list(range(2,11,2))
print(even_numbers)

#list comprehension (combining a for loop)
#prints out the values of 1-10 squared
squares=[value**2 for value in range(1,11)]
print(squares)

#list slicing
#prints out the first 3 players of the list
#starts at 0 ends at 2 (does not include 3)
players=['charles','martina','michael','florence','eli']
print(players[0:3])

#if you omit the first number before the colon it starts
#at the beginning of the list
print(players[:4])

#slice that includes the end of a list
#starting with index 2
print(players[2:])

#looping through a slice
players=['charles','martina','michael','florence','eli']
print("Here are the first three players on my team")
for player in players[:3]:
    print(player.title())

#copying a list
my_foods=['pizza','donuts','carrot cake']
friend_foods=my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

#provind we have two separate lists
my_foods.append('gabagool')
friend_foods.append('ice cream')

print("\n")

print("My favorite foods are ")
print(my_foods)
print("\nMy friends favorite foods are")
print(friend_foods)
print("\n")
#tuples (immutable lists)
dimensions=(200,50)
print(dimensions[0])

#writing over a tuple, assigning a new value to a variable
#redefining the whole tuples

dimensions=(200,50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions=(400,150)
print("\nModified dimensions: ")
for dimension in dimensions:
    print(dimension)
