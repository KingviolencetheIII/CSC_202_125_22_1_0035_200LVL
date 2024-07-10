import random

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random()  # Interval is between 0 and 1
print(random_float)

random_float = random.random() * 5
print(random_float)

love_score = random.randint(1, 100)
print(f"Your love is {love_score}")

states_of_america = [
    "Delaware",
    "Pencilvania",
    "New Jersey",
    "Georgia",
    "Connecticut",
    "Massachusetts",
    "Maryland",
    "South Carolina",
    "New Hampshire",
    "Virginia",
    "New York",
    "North Carolina",
    "Rhode Island",
    "Vermont",
    "Kentucky",
    "Tennessee",
    "Ohio",
    "Louisiana",
    "Indiana",
    "Mississippi",
    "Illinois",
    "Alabama",
    "Maine",
    "Missouri",
    "Arkansas",
    "Michigan",
    "Florida",
    "Texas",
    "Iowa",
    "Wisconsin",
    "California",
    "Minnesota",
    "Oregon",
    "Kansas",
    "West Virginia",
    "Nevada",
    "Nebraska",
    "Colorado",
    "North Dakota",
    "South Dakota",
    "Montana",
    "Washington",
    "Idaho",
    "Wyoming",
    "Utah",
    "Oklahoma",
    "New Mexico",
    "Arizona",
    "Alaska",
    "Hawaii",
]

print(states_of_america)

print(states_of_america[0])  # starting from the first to the last

print(states_of_america[1])

print(states_of_america[-1])  # starting from the last to the first

states_of_america[1] = "Pennsylvania"
print(states_of_america)

states_of_america.append("Nigeria")
print(states_of_america)

states_of_america.extend(["Adil State", "Angelaland", "Jack Bauer Land"])
# print(states_of_america)

dirty_dozen = [
    "Strawberries",
    "Spinach",
    "Kale",
    "Nectarines",
    "Apples",
    "Grapes",
    "Peaches",
    "Cherries",
    "Pears",
    "Tomatoes",
    "Celery",
    "Potatoes",
]

fruits = [
    "Strawberries",
    "Nectarines",
    "Apples",
    "Grapes",
    "Peaches",
    "Cherries",
    "Pears",
]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)
