# importing datetime module for now()

import datetime
from datetime import date

class Person:
  def __init__(self, name, birthdate):
    self.name = name
    self.birthdate = birthdate


franks_birthday = Person("Frank", date(1985, 6, 1))
lucies_birthday = Person("Lucie", date(1999, 7, 3))
johns_birthday = Person("John", date(1972, 2, 22))

#Creating an array of birthdays
birthdays = [franks_birthday,lucies_birthday, johns_birthday]


# using now() to get current time
current_time = datetime.datetime.now()

# Printing value of now.
print("Time now at greenwich meridian is:", current_time)

#Prints the number of days between now and the new year 

from_date = date(current_time.year,current_time.month,current_time.day)
to_date = date(2024, 1, 1)
delta = to_date - from_date
print(delta.days)

# Creating an array of birthdays
birthdays = [franks_birthday, lucies_birthday, johns_birthday]

#Printing the next birthday
def get_next_birthday(birthdays):
    today = datetime.date.today()
    next_birthday = None
    for person in birthdays:
        # Check if the birthday for this year has already passed, if yes, use the next year's birthday
        this_year_birthday = date(today.year, person.birthdate.month, person.birthdate.day)
        if this_year_birthday < today:
            this_year_birthday = date(today.year + 1, person.birthdate.month, person.birthdate.day)
        
        if next_birthday is None or this_year_birthday < next_birthday:
            next_birthday = this_year_birthday
    
    return next_birthday 

#Time till next birthday 

next_birthday = get_next_birthday(birthdays)
print("Next birthday:", next_birthday)

def time_till_next_birthday(next_birthday):
    today = datetime.datetime.now()
   
    next_birthday_date_time = datetime.datetime(next_birthday.year, next_birthday.month, next_birthday.day)
    time_till_birthday = next_birthday_date_time - today
    return time_till_birthday

next_birthday = get_next_birthday(birthdays)
print("Next birthday:", next_birthday)

time_till_birthday = time_till_next_birthday(next_birthday)
print("Time till next birthday:", time_till_birthday)




 
