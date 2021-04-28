"""
Storing your Functions in modules
    One advantage of functions is the way they separate blocks of code form your main program. By using descriptiove names for your functions, your
    main program. By using descriptive names for your functions, your main program will be much easier to follow. You can go a step further by storing your
    functions in a separate file called a module and then importing that module into your main program. An import statement tells Python to make
    the code in a module available in the currently running program file. 
"""

"""Importing an entire module
    To start importing functions, we first need to create a module. A module is a file engin in the .py that contains the code you want to import into
    your program. 
"""

def make_pizza(size,*toppings):
    """Summarize the pizza we are baout to make."""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

