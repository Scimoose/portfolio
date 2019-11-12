from bs4 import BeautifulSoup
import requests
import json


print("What you want to search for?")
search_for = input()
str = "https://www.ncbi.nlm.nih.gov/pubmed/?term=" + search_for.replace(" ", "+")

# This script scrapes the website for the content of interest
page = requests.get(str)

soup = BeautifulSoup(page.content, 'html.parser')

# this line grabs the NCBI search results (only 3 now sadly, the "best results") and returns text
text = soup.find_all('div', class_='sensor_content')[0].get_text()

# strings cleanup, returns a dict with title, year and author
arr = text.split("\n", 100)

arr = list(filter(None, arr))
arr.pop()

print("\nTop 3 searches:\n")
print("Title:", arr[0], "\nAuthor:", arr[1])
print("\nTitle:", arr[3], "\nAuthor:", arr[4])
print("\nTitle:", arr[6], "\nAuthor:", arr[7])

input('Press Enter to exit')
'''
# this is the part which is responsible for saving the data in .json
data = {
    "firstTitle": arr[0],
    "firstAuthor": arr[1],
    "firstYear": arr[2],
    "secTitle": arr[3],
    "secAuthor": arr[4],
    "secYear": arr[5],
    "thirdTitle": arr[6],
    "thirdAuthor": arr[7],
    "thirdYear": arr[8],
}
print(data)
# Saves a python dict object to JSON format file.
def python_dict_to_json_file(file_path):
    try:
        # Gets a file object with write permission.
        file_object = open(file_path, 'w')
        # Saves dict data into the JSON file.
        json.dump(data, file_object)
        print(file_path + " created. ")
    except FileNotFoundError:
        print(file_path + " not found. ")

if __name__ == '__main__':
    python_dict_to_json_file("./data.json")
'''
