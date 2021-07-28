
def value_lost ()
value = 2000
dep = 0.1
year = 2021
Depreciation=0.1
while value >= 1000:
    value -= (value*0.1)
    year = year + 1
    print(year, value)
