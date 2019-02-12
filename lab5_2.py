from types import *

def isValidDate(year, month, day):
    """assert type(month) is IntType, "month is not an int: %r" % month
    assert type(year) is IntType, "year is not an int: %r" % year 
    assert type(day) is IntType, "day is not an int: %r" % day"""
    assert year>=1901 and year<=2020, "Years must be in range from 1901-2020"
    assert month>=1 and month<=12, "Months must range from 1-12"
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    #check if year is leap year
    if year%4 == 0 and (not year%100 == 0 or year%400 == 0):
        months[1] = 29
    assert day>=1 and day<=months[month-1], "The day must be in the range of 1-%d" % months[month]
    print("Success! You entered a valid date!")
    
def main():
    flag = True
    while flag:
        try:
            date = list(map(int, input("Please enter a valid date in the format of YYYY-MM-DD: ").split("-")))
            isValidDate(date[0],date[1],date[2])
        except AssertionError as err:
            print("Looks like you entered an invalid date, the issue was: ", err.args)
        except ValueError as err:
            print(err.args)
        else:
            flag = False
        
main()