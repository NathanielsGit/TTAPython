
num1 = input("Enter the first number")
num2 = input("Enter the second number")
num3 = input("Enter the third number")
num4 = input("Enter the fourth number")

numbers = [num1,num2,num3,num4]


my_file = open("numbers_file.txt", "w")
my_file.write (num1)
my_file.write (num2)
my_file.write (num3)
my_file.write (num4)

my_file.close()
