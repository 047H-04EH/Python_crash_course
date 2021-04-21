"""The input function:
	The input() function pauses your program and waits for the user to enter some text. One Python receives the user's input, 
	it stores it in a variable to make it conveinent for you to work with. 
 """

message=input("Tell me something, and I will repeat it back to you: ")
print(message)

"""Using int() to Accept Numerical Input 
	When you use the input() function, Python interprets everything the user enters as a string. We can resolve this issue by using
	the int() function, whicih tells Python to treat the input as a numerical value. The int() function converts a string representation
of a number to a numerical representation.
"""

age=input("How old are you? ")
age=int(age)
bool=age>=18
print(bool)

"""The modulo operator: 
	(%) divides one number by another number and returns the remainder. You can use to determine if a number is 
	even or odd
"""

number=input("Enter a number, and i'll tell you if it's even or odd: ")
number=int(number)

if number % 2 == 0:
	print("\nThe number " +str(number) + " is even.")
else: 
	print("\nThe number " + str(number)+ " is odd.")

"""Accepting input in Python 2.7 
	If you're using Python 2.7 you should use the raw_input() function when prompting for user input. 
	This function interprets all input as a string, just as input() does in Python3. 
"""

"""While loop introduction: 
	You can use a while loop to count up through a series of numbers. For example, 
	The following while loop counts from 1 to 5: 
"""

current_number=1
while current_number <=5: 
	print(current_number)
	current_number+=1

"""While loop, letting the user choose when to quit. 
	We can make a program run as long as the user wants by putting most of the program inside a hwile loop. We'll define a quit value
	and then keep the program running as long as the user has not entered the quit value. 
"""

prompt="\nTell me something, and i will repeat it back to you: "
prompt+="\nEnter 'quit' to end the program. "
message=""

while message!='quit':
	message=input(prompt)
	print(message)

print("\n")
"""Using a flag: 
	For a program that should run only as long as many condtions are true, you can define one variable that 
	determines whether or not the entire program is active. This variable, called a flag, acts as a singal to 
	the program
"""

prompt="\nTell me something, and I  will repeat it back to you: "
prompt+= "\nEnter 'quit' to end the program. "

active=True
while active: 
	message=input(prompt)

	if message == 'quit':
		active=False
	else: 
		print(message)


print("\n")
"""Using break to Exit a loop: 
	To exit a while loop immediately without running any remaining code in the loop, regardless of the results
	of any conditional test, use the break statement. The break statement directs the flow of your program; 
	You can use it to control which lines of code are executed and which aren't, so the program only executes 
	code that you want it to, when you want it to. 
"""


prompt="\nPlease enter the name of a city you have visited: "
prompt+= "\nEnter 'quit' when you are finished. "

while True: 
	city=input(prompt)

	if city == 'quit':
		break
	else:
		print("I'd love to go to " + city.title() + "!")


print("\n")
"""Using continue in a loop: 
	Rather than breaking out of a loop entirely without executing the rest of its code, you can use the continue
	statement to return to the beginning of the loop based on the result of a conditional test. For example, 
	consider a loop that counts from 1 to 10 but pritns only the odd numbers in that range. 
"""

current_number=0
while current_number<10:
	current_number+=1
	if current_number %2==0:
		continue
	print(current_number)
	

"""Using a while loop with lists and dictionaries:
	Consider a list of newly registered but unverified users of a website. After we verify these users, how can we move them to a separate
	list of confirmed users? One way would be to use a while loop to pull users from the list of unconfirmed users as we 
	verify them and then add them to a separate list of confirmed users. 
"""

#Start with users that need to be verified, 
#And an empty list to hold confirmed users. 

unconfirmed_users=['alice','brian','candace']
confirmed_users=[]

#verify each user until there are no more unconfirmed users. 
# Move each verfied user into the list of confirmed users. 

while unconfirmed_users: 
	current_user=unconfirmed_users.pop()

	print("Verifying user: "+current_user.title())
	confirmed_users.append(current_user)

#Display all confirmed users
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())

"""Explanation of user verification example:
	WE begin with a list of unconfirmed users (Alice, Brian, and Candace) and an empty list to hold confimed users. 
	The while loop runs as long as the list unconfirmed_users is not empt. Within this loop, the pop() function
	removes unverified users one at a time from the end of unconfirmed_users. Here, because Candace is last in the
	unconfirmed_users list, her name will be the first to be removed, stored in current)user, and added to the
	confimed_users list. Next is Brain then alice. 
"""

"""Removing all instances of Specific values from a list:
	Say you have a list of pets with the value 'cat repeated several times. To remove all instances of that value, you
	can run a while loop until 'cat' is no longer in the list. 
"""

pets=['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets: 
	pets.remove('cat')

print(pets)


"""Filling a Dictionary with User Input: 
	You can prompt for as much input as you need in each pass through a while loop. 
	Lets make a polling program in which each pass through the loop prompts for the participant's name and response
	We'll store the data we gather in the dicationary, because we want to connect each response with a particular user.
"""

responses={}

#Set a flag to indicate that polling is active. 
polling_active=True

while polling_active:
	#prompt for the person's name and response
	name=input("\nWhat is your name? ")
	response=input("Which mountain would you like to climb someday? ")

	#Store the reponse in the dictionary. 
	responses[name]=response

	#find out if anyone else is going to take the poll
	repeat=input("Would you like to let another person response? (yes/no) ")
	if repeat=='no':
		polling_active=False

#polling is complete. Show the results. 
print("\n--- Poll results---")
for name, response in responses.items():
	print(name+ " would like to climb " + response + ".")

"""Explanation of polling example: 
	The program first defines an empty dictionary (responses) and sets a flag (polling_Active) to indicate that polling is active. 
	As long as polling_active is True, Python will run the code in the while loop. Within the loop, the user is prompted
	to enter their username and a mountain they'd like to climb. That information is stored in the responses dictionary
	and the user is asked whether or not to keep the poll running. If they enter yes, the program enters the while loop
	again. If they enter no, the polling_active flag is set to False, the while loop stops running, and the final 
	code block displays the results of the poll. 
"""


