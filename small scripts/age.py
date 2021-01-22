# the code takes your age and returns some facts about it
import datetime

print("Hello")
print("How old are you?")

date_entry = input('Enter a date in YYYY-MM-DD format ')
year, month, day = map(int, date_entry.split('-'))

date1 = datetime.date(year, month, day)
diff = datetime.date.today() - date1

print("You lived for " + str(diff.days/30.45) + " months")
print("That's " + str(diff.days) + " days")
print("And " + str(diff.days*24) + " hours!")
print("So far so good.")

#TODO \/
#print("In the year you were born " +  + " happened.")


input('Press Enter to exit')


#testy jednostkowe
#print(year)
#print(month)
#print(day)
#print(date1)
