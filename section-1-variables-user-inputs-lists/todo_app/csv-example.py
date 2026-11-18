import csv

with open("files/weather.csv") as file:
    data = list(csv.reader(file))

city = input("Enter a city: ")
for row in data:
    if city.lower() == row[0].lower():
        temperature = row[1]
        print(f"Temperature: {temperature}")
