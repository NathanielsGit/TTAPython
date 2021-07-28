#Write a program that asks a user for their favourite number between 1 and 100 and then tells them a joke based on the number.
#You should use a minimum of 3 jokes

name = str(input("Please enter your name "))
print("hi " + name, "enter a number between 0 and 100 to hear a joke")
num = int(input("choose your number here "))
if num == 0:
    print("you entered {0}, thanks for nothing!".format(num))
elif num % 2 == 0 and num <= 100:
    print("you entered {0}, What did the even number say when it saw a room full of primes? two can play this game!".format(num))
elif num % 2 == 1 and num <= 100:
    print("you entered {0}, I challenged the number 1 to a fight. When 1 showed up, he brought 3, 5, 7 and 9, the odds were against me!".format(num))
else:
    print("number out of range, please try again!!")





