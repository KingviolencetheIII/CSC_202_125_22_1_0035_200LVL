# MINE

student_heights = input("Input a list of student heights ").split()
sum = 0
length = 0

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

print(student_heights)

for n in student_heights:
    sum += n
    length += 1

average = round(sum / length)

print(f"Sum of all the Student's heights is {sum}")

print(f"Number of Students is {length}")

print(f"Average height of the students is {average}")

# LESSON

total_height = sum(student_heights)
number_of_student = len(student_heights)
average_height = round(total_height / number_of_student)
print(average_height)
