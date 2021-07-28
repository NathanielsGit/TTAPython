value = 2000
year = 2021

def Asset_Value (value, year):
    while value >= 1000:
        value -= (value*0.1)
        year = year + 1
        print(year, value)
print ("Value per year as asset depreciates by 10% P/A")
Asset_Value(value=2000,year=2021)