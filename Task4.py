#A motorbike costs £2000 and loses 10% of its value every year.
# Using a loop, print the value of the bike every following year until it falls below £1000

value = 2000
year = 2021
while value >= 1000:
    value -= (value*0.1)
    year = year + 1
    print(year, value)

