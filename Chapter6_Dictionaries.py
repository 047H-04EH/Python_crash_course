#sample dictionary
alien_0={'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])
print("\n")

#adding new key value pairs
alien_0={'color':'green', 'points':5}
print(alien_0)
alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)
print("\n")

#starting with an empty dictionary and adding values individually
alien_0={}
alien_0['color']='green'
alien_0['points']=5
print(alien_0)
print("\n")

#modifying values in a dictionary
alien_0={'color':'green'}
print(alien_0['color'])
alien_0['color']='yellow'
print(alien_0['color'])
print("\n")

"""Track the position of an alien that can move at different speeds
we'll store a value representing the alien's current speed
and then use it to determine how far
to the right the alien should move"""

alien_0={'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: "+str(alien_0['x_position']))

#move the alien to the right
#determine how far to move the alien
#based on its current speed
if alien_0['speed']=='slow':
    x_increment=1
elif alien_0['speed']=='medium':
    x_increment=2
else:
    #this must be a fast alien
    x_increment=3

#the new position is the old position plus the increment
alien_0['x_position']=alien_0['x_position']+ x_increment
print("New x-position: "+ str(alien_0['x_position']))
print("\n")

#removing key value pairs
alien_0={'color':'green','points':5}
print(alien_0)
del alien_0['points']
print(alien_0)

#looping through all key value pairs
user_0={
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}
for key,value in user_0.items():
    print("\nKey: "+key)
    print("Value: "+value)
print("\n")
#looping through all keys in a dictionary
favorite_languages={
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
for name in favorite_languages.keys():
    print(name.title())
#looping through a dictionary's keys in order
favorite_languages={
'jen': 'python',
'sarah':'c',
'edward':'ruby',
'phil':'python',
}
for name in sorted(favorite_languages.keys()):
    print(name.title()+" Thank you for taking the poll."
)

#looping through all values in a dictionary
favorite_languages={
'jen':'python',
'sarah':'c',
'edward':'ruby',
'phil':'python',
}

print("The following languages have been mentioned: ")
for language in favorite_languages.values():
    print(language.title())

#nesting: a list of dictionaries
alien_0={'color':'green','points':5}
alien_1={'color':'yellow','points':10}
alien_2={'color':'red','points':15}
aliens=[alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)

#nesting: a list in a dictionary
#store informatino about a pizza being ordered
pizza={
'crust':'thick',
'toppings':['mushroom','extra cheese'],
}
#summarize the order
print("You ordered a "+pizza['crust']+"-crust pizza"+" With the following toppings: ")
for topping in pizza['toppings']:
    print("\t "+topping)

#nesting: a dictionary inside a dictionary
users={
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton'
        },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
        },
}
for username, user_info in users.items():
    print("\nUsername: "+username)
    full_name=user_info['first']+ " "+user_info['last']
    location=user_info['location']

    print("\tFull name: "+full_name.title())
    print("\tLocation: "+location.title())
