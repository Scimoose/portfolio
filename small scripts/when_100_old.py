# Create a program that asks the user to enter their name and their age.
name = input("Tell me your name: ")
age = input("Tell me your age: ")

# Calculate the year they will turn 100.
year = 2020 - int(age) + 100

# Print out a message addressed to them that tells them the year that they will turn 100 years old.

if year < 2020:
    print("You already turned 100 in year", year, name)
else:
    print(name + ", you will turn 100 in the year", year)
