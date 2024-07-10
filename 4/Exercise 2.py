import random

names_string = input(f"Give me everybody's names, seperated by a comma. ")

names = names_string.split(", ")

# LONG METHOD

num_items = len(names)

random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]

print(f"{person_who_will_pay} is going to pay for the meal today.")

