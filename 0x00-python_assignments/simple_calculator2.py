import datetime

def get_date_difference(current_date, birthday):
    # Convert the input strings to date objects
    current_date = datetime.datetime.strptime(current_date, "%Y-%m-%d")
    birthday_date = datetime.datetime.strptime(birthday, "%Y/%m/%d")

    # Calculate the age
    age = current_date - birthday_date

    # Calculate years, months, and days
    years = age.days // 365
    months = (age.days % 365) // 30
    days = (age.days % 365) % 30

    return years, months, days

name = input("Enter your name: ")
birthday = input("Please enter your birthday (YYYY/MM/DD): ")

current_date = datetime.date.today().strftime("%Y-%m-%d")
years, months, days = get_date_difference(current_date, birthday)

print(f"Hello, {name}!")
print(f"You are {years} years, {months} months, and {days} days old.")
