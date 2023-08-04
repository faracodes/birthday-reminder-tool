# importing datetime module for now()

import datetime
from datetime import date

class Person:
  def __init__(self, name, birthdate):
    self.name = name
    self.birthdate = birthdate

#This function gets the next birthday and prints out multiple birthdays on the same date 
def get_next_birthday(birthdays):
    today = datetime.date.today()
    next_birthday = None
    next_birthday_names = []

    for person in birthdays:
        # Check if the birthday for this year has already passed, if yes, use the next year's birthday
        this_year_birthday = date(today.year, person.birthdate.month, person.birthdate.day)
        if this_year_birthday < today:
            this_year_birthday = date(today.year + 1, person.birthdate.month, person.birthdate.day)
        
        if next_birthday is None or this_year_birthday < next_birthday:
            next_birthday = this_year_birthday
            next_birthday_names = [person.name]
        elif this_year_birthday == next_birthday:
            next_birthday_names.append(person.name)
    
    return next_birthday, next_birthday_names


#Returns the time till next birthday
def time_till_next_birthday(next_birthday):
    today = datetime.datetime.now()
   
    next_birthday_date_time = datetime.datetime(next_birthday.year, next_birthday.month, next_birthday.day)
    time_till_birthday = next_birthday_date_time - today
    return time_till_birthday


franks_birthday = Person("Frank", date(1985, 6, 1))
lucies_birthday = Person("Lucie", date(1999, 7, 3))
johns_birthday = Person("John", date(1972, 2, 22))
suzies_birthday = Person("Suzie", date(2002, 2, 22))

#Creating an array of birthdays
birthdays = [franks_birthday,lucies_birthday, johns_birthday, suzies_birthday]

next_birthday , person_names = get_next_birthday(birthdays)
print(f"Next birthday on {next_birthday}: {', '.join(person_names)}")


time_till_birthday = time_till_next_birthday(next_birthday)

#Countdown Format 
days = time_till_birthday.days
hours, remainder = divmod(time_till_birthday.seconds, 3600)
minutes, seconds = divmod(remainder, 60)

print(f"Time till next birthday: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds.")


 
