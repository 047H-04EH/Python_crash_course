"""Defining a function: 
        Here's a simple function named greet_user() that prints a greeting.
"""

def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()

"""Explanation of Defining a function: 
    The keyword def informs Python that you're defining a function. This is the function definition, which tells python the name 
    of the function and, if applicable, what kind of information the function needs to do its job. 
    The parenthesis hold that information. In this case, the name of the function is greet_user(), and it needs no more information
    to do its job, so its parentheses are empty. Any indented lines that follow def greet_user(): make up the body of the function. 
    The text in quitations is called a docstring, which describes what the function does. Docstrings are enclosed in triple quites, which 
    Python looks for when it generates documentation for the functions in your pgorams.The print("Hello) is the only line of actual code
    in the body of this function, so greet)user() has just one job: print("Hello"). When you want to use this function, you call it. A
    function call tells python to execute the code in the function. To call a function, you write the name of the function, follwed by
    any necessary information in parenthesies. BEcause no information is needed here, calling our function is as sinmple as entering
    greet_user(). as expected it prints hello. 

"""

"""Passing information to a function: 
    For the function to greet the user by name, you enter username in the parenthesis of the function's definition at def greet_user(). 
    By adding username here you allow the function to accept any value of username you specify. This function now expects you to 
    provide a value for username each time you call it. When you call greet_user(), you can pass it a name, such as 'jesse'
    inside the parenthesis
"""

def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")

greet_user('jesse')

"""Positional Arguments: 
    When you call a function, Python must match each argument in the function call with a parameter in the function definition. 
    The simplest way to do this is based on the order of the arguments provides. Values matched up this way are called positional
    arguments. 
"""

def describe_pet(animal_type,pet_name):
    """Display information about the pet"""
    print("\nI have a " + animal_type + ".")
    print("\nMY " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster','harry')

"""Multiple function calls:
    You can call a function as many times as needed. Describing a second, different pet requires just one more call to describe_pet():
"""
def describe_pet(animal_type,pet_name):
    """Display information about the pet"""
    print("\nI have a " + animal_type + ".")
    print("\nMY " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster','harry')
describe_pet('dog','willie')

"""Default values: 
    When writing a function, you can define a default value for each parameter. If an argument for a parameter is provided
    in the function call, Python uses the argument value. If not, it uses the parameter's default value. So when you define
    a default value for a parameter, you can exclude the corresponding argument you'd usually write in the function call. 
    Using default values can simplify your functino calls and calfigy the ways in which your functions are typically used. 
"""

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet"""
    print("\nI have a " + animal_type + ".")
    print("\nMY " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='willie')

"""Return values description:
    A function doesn't always have to display its output directly. Instead, it can process some data and then return a value or set of values. 
    The value the function returns is called a return value. The return statement takes a value from inside a function and sends it back to the line that called 
    the function. Return values allow you to move much of your program's grunt work into funcitons, which can simplify the body of your program.
"""

"""Returning a Simple Value: 
    Lets look at a function that takes a first and last name, and returns a neatly formatted full name: 
"""

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name=first_name + ' ' + last_name
    return full_name.title()

musician=get_formatted_name('jimi','hendrix')
print(musician)

"""Making an argument optional:
    Sometimes it makes sense to make an argument optional so that people using the function can choose to provide extra information only if they want to. 
    You can use default values to make an argument optional.
"""

def get_formatted_name(first_name,last_name,middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name=first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name=first_name + ' ' + last_name
    return full_name.title()

musician=get_formatted_name('jimi','hendrix')
print(musician)

musician=get_formatted_name('john','hooker','lee')
print(musician)


"""Returning a Dictionary:
    A function can return any kind of value you need it to, including more complicated data structures like
    lists and dictionaries. For example, the following function, takes in part of a name and returns a 
    dictionary representing a person:
"""

def build_person(first_name,last_name):
    """Return a dictionary of information about a person"""
    person={'first':first_name,'last':last_name}
    return person

musician=build_person('jimi','hendrix')
print(musician)

"""
Using a function with a while loop:
    You can use functions with all the Python structures you've learned about so far. For example, let's
    use the get_formatted_name() function with a while loop to greet users more formally.
def get_formatted_name(first_name, last_name):
    REturn a full name, neatly formatted.
    full_name=first_name + ' ' + last_name
    return full_name.title()
"""
"""
#this is an infinite loop!
while True:
    print("\nPlease tell me your name: ")
    f_name=input("First name: ")
    l_name=input("Last name: ")

    formatted_name=get_formatted_name(f_name,l_name)
    print("\nHello, " + formatted_name+ "!")
"""

"""For this example we use a simple version of get_formatted_name() that doesnt involve middle names. 
    The while loop asks the user to enter their name, and we prompt for their first and last name separately. 
    But theres one problem with this while loop: We havent defined a quit condition. Where do you put a 
    quit condition when youask for a series of inputs? We want the user to bea ble to quit as easily as possible, so each prompt should offer a way to quit. The break statement offers a straight-forward way to exit
    the loop at either prompt:
"""

def get_formatted_name(first_name, last_name):
    REturn a full name, neatly formatted.
    full_name=first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name: ")
    print("(enter 'q' at any time to quit)")

    f_name=input("First name: ")
    if f_name=='q':
        break

    l_name=input("Last name: ")
    if l_name=='q':
        break
    
    formatted_name=get_formatted_name(f_name,l_name)
    print("\nHello, " + formatted_name + "!")

"""

"""
Passing a list:
    Youll often find it useful to pass a list to a function, whether its a list of names, numbers 
    or more complex objects, such as dictionaries. When you pass a list to a function, the funciton gets 
    direct access to the contents of the list. Lets use functions to make working with lists more
    efficient. Say we have a list of users and want to print a greeting to each. The following example
    sends a list of names to a function called greet_users() which greets each person in the list 
    individually. 
"""

def greet_users(names):
    """print a simple greeting to each user in the list."""
    for name in names:
        msg="Hello, " + name.title() + "!"
        print(msg)

usernames=['hannah','ty','margot']
greet_users(usernames)

"""
Passing an Arbitrary Number of Arguments:
    Sometimes you wont know ahead of time how many arguments a funciton needs to aaccept. 
    Fortunately, Python allows a function to collect an arbitrary number of arguments from the calling 
    statement. For example, consider a function that builds a pizza. It needs to accept a number of 
    toppings, but you cant know ahead of time how many toppings a person will want. The function in the following example has one parameter. *toppings, but this parameter collects as many arguments as the calling line provides
"""

print("arbitraty arguments")
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- "+topping)
make_pizza('pepperoni')
make_pizza('mushrooms','green pepper','extra cheese')



