#loops through a list and prints the item in
#all caps if the condition is met
cars=['audi','bmw','subaru','toyota']

for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())

#using and to check multiple conditions
#both conditions must be true for it to return true
age_0=22
age_1=18
bool=age_0>= 21 and age_1 >=21
print(bool)

#using or to check multiple conditions
#one condition must be true to returen true
age_0=22
age_1=18
bool=age_0>=21 or age_1>=21
print(bool)

#checking whether values are in or not in a list
requested_toppings=['mushrooms','onion','pineapple']
bool='mushrooms' in requested_toppings
print(bool)

banned_users=['andrew','carolina','david']
user='marie'
if user not in banned_users:
    print(user.title()+" you can post a reponse if you wish.")

#if else statement user is under 18 so prints out
#you are too young to vote
age=17
if age>=18:
    print("you are old enough to vote")
    print("Have you registered to vote yet?")
else:
    print("Sorry you are too young to vote")
    print("Please register to vote as soon as you are 18")

#if elif else chain
#can give multiple conditions instead of just an if else
#use this when it is only important to test until it passed
#once it passes the other conditions are not checked
age=12
if age<4:
    print("Your admission cost is 0")
elif age <18:
    print("Your admission cost is $5")
else:
    print("Your admission cost is $10")

#to check all the conditions use multiple if statements
requested_toppings=['mushrooms','extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")
print("\nFinished making your pizza")
print("\n")

#checking special items in a list
requested_toppings=['mushrooms','green peppers','extra cheese']

for requested_toppings in requested_toppings:
    if requested_toppings =='green peppers':
        print("Sorry, we are out of green peppers right now")
    else:
        print("Adding "+ requested_toppings)
print("\nFinished making your pizza")

#checking that a list is not empty
#we do a quick check at line 81, when the name of a list
#is used in an if statement, python returns True if the list
#contains at least one item, an empty list evaluates to False
#if requested_toppings passes the conditional test, we run
#the same for loop we used in the previous example
#if the conditional test fails we print a message asking the customer if they
#really want a plain pizza with not toppings
requested_toppings=[]
if requested_toppings:
    for requested_toppings in requested_toppings:
        print("Adding" + requested_toppings)
    print("\nFinished making your pizza")
else:
    print("are you sure you want a plain pizza?")
