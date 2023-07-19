# Getting current date and time using now().

# importing datetime module for now()
import datetime

# using now() to get current time
current_time = datetime.datetime.now()

# Printing value of now.
print("Time now at greenwich meridian is:", current_time)

#Printing out the distance between 19/07/23 and 01/01/24 
from datetime import date
f_date = date(2023, 7, 19)
l_date = date(2024, 1, 1)
delta = l_date - f_date
print(delta.days)
