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

f_date = date(current_time.year,current_time.month,current_time.day)
l_date = date(2024, 1, 1)
delta = l_date - f_date
print(delta.days)


 
