## Birthday Countdown Application

The Birthday Countdown Application is a Python script that calculates and displays the time remaining until the next birthday for a list of people. The countdown format includes days, hours, minutes, and seconds. This application is useful for reminding you of upcoming birthdays and how much time is left to prepare for the celebration.

### Prerequisites

Before running the application, make sure you have the following:

1. Python installed on your computer. You can download Python from the official website: https://www.python.org/downloads/

### Getting Started

1. Download the Python script `birthday_countdown.py` from the repository.
2. Place the script in a convenient location on your computer.

### Usage

1. Open a terminal or command prompt.
2. Navigate to the location where you saved the `birthday_countdown.py` script.

#### Defining Birthdays

In the script, you can define the birthdays of the people you want to track. To add new people and their birthdays, follow this example:

```python
# Create a new instance of the Person class for each individual
person_name = Person("Person Name", date(YEAR, MONTH, DAY))
```

Replace `"Person Name"` with the individual's name and set the `YEAR`, `MONTH`, and `DAY` with their birthdate.

```python
franks_birthday = Person("Frank", date(1985, 6, 1))
lucies_birthday = Person("Lucie", date(1999, 7, 3))
johns_birthday = Person("John", date(1972, 2, 22))
```

3. Add these person instances to the `birthdays` list:

```python
birthdays = [franks_birthday, lucies_birthday, johns_birthday]
```

#### Running the Application

To run the Birthday Countdown Application, execute the following command in the terminal:

```bash
python birthday_countdown.py
```

The application will then display the next birthday and the time remaining in the countdown format for each person defined in the `birthdays` list.

### Example Output

```
Next birthday: 2023-08-17
Time till next birthday: 14 days, 5 hours, 28 minutes, 42 seconds.
```

### Notes

- The countdown considers only the current year's birthday. If the birthday has already passed this year, the countdown will display the time remaining for the next year's birthday.
- The application uses the local time on your computer (the timezone where it is running) to calculate the countdown.

### Customization

You can modify the `birthdays` list to include different individuals and their respective birthdates. Additionally, you can enhance the script to include more advanced features or integrate it with other applications.

### Conclusion

The Birthday Countdown Application is a simple yet useful tool for tracking upcoming birthdays and calculating the time remaining for each one. Enjoy keeping track of your friends' and family members' special days and ensure you have enough time to prepare for their celebrations!

by Fara Ifaturoti and Oli Haley