#Working with user input and while loop
"""
for user inputs
- Will write a program that will ask a user an input and work with that input
-Will use input() function to get the user input
"""
#Program below ask  user their age and check if the user is legible to vote, please note  standard age is 18 years old
current_year = 2026
user_age = int(input("When are you born? "))
age = abs(current_year - user_age)
age_to_vote = abs(age - 18)
if age >= 18:
    print("You can proceed to voting station")
else:
    print(f"You are NOT old enough to vote \nTry in {age_to_vote} years, in {user_age+age_to_vote} instead")
#This program above will ask the user the year at which user was born, and then check if the user is old enough to vote, if not it will tell the user how many years they need to wait and how many years they have already waited.
#This is a simple input() function program.
"""
Try it yourself
7-1. Rental Car: Write a  program that asks the user what kind of rental  car they would like. Print a message about that car, such as 'Let me see if i can find you a {user's car choice} car.'

7-2. Restaurant: Write a program that asks the user how many people are in  their dinner group. If the answer is more than 8, print message saying  they'll have to wait for a table. Otherwise, report that their table is ready.

7-3. Multiples of Ten:  Ask the user for a number, an then report whether the number is a multiple of ten or not.

"""

#7-1

car_choice = input("What kind of car would you like to rent? ")
print(f"Let me see if i can find you a {car_choice} car.")

#7-2
pep_in_group= int(input("How many people are in your group? "))
if pep_in_group > 8:
    print("You'll have to wait for a table")
else:
    print("Your table is ready")
    
#7-3
multiple_of_ten = int(input("What is the number? "))
if multiple_of_ten % 10 == 0:
    print("It's a multiple of ten")
else:
    print("It's not a multiple of ten")





