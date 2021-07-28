#Write a program that allows the user to enter their favourite starter, main course, dessert and drink
#Concatenate these and output the message –“Your favourite meal is...with a glass of...

Name = input("Please enter your name... ")
Starter = input("What would you like for your starter... ")
Main_course = input("What would you like for your main course... ")
Dessert = input("Please choose a dessert...")
Drink = input("What drink would you like with your meal...")
print("thanks for joining us " + Name)
print("your favorite meal based on your selection is " + Starter + " with " + Main_course + " as your main dish, " + "followed by " + Dessert + " for Dessert " + "and a glass of" + Drink + " as your choice of drink")