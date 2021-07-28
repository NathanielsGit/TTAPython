#Write a program that does the following:
#a)Stores a random number (1-10) in a variable
#b)Asks a user for their name and stores this in a variable
#c)Asks a user to guess the number between 1 and 10.
#d)Tells the user whether they have guessed correctly

Name = input("Please enter your name here: ")
print("Hi " + Name + ", thank you for purchasing a ticket to this lucky draw raffle, enter a number between 1 and 10 for a chance to win")
Number = int(input("Enter a Number of your choice: "))
from random import seed
from random import randint
seed(1)
for _ in range(10):
    value = randint(0,10)
if Number == value :
    print("Congratulations, you guessed it... ")
else :
    print("Close enough but not quite, the number is " + str(value) +" better luck next time...")
    print("Would you like to try again ?")