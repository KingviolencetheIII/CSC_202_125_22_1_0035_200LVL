row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

a = int(position[0])
b = int(position[1])
if b == 1:
    if a == 1:
        row1 = ["X", "⬜", "⬜"]
    elif a == 2:
        row1 = ["⬜", "X", "⬜"]
    elif a == 3:
        row1 = ["⬜", "⬜", "X"]
if b == 2:
    if a == 1:
        row2 = ["X", "⬜", "⬜"]
    elif a == 2:
        row2 = ["⬜", "X", "⬜"]
    elif a == 3:
        row2 = ["⬜", "⬜", "X"]
if b == 3:
    if a == 1:
        row3 = ["X", "⬜", "⬜"]
    elif a == 2:
        row3 = ["⬜", "X", "⬜"]
    elif a == 3:
        row3 = ["⬜", "⬜", "X"]

print(f"{row1}\n{row2}\n{row3}")


# LESSON

horizontal = int(position[0])
vertical = int(position[1])


selected_row = map[vertical - 1]
selected_row[horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")

# OR

map[vertical - 1][horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")
