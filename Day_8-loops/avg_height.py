# fruits = ["Apple", "Banana", "orange"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + "pai")
#[178, 160, 188, 140, 150, 159, 166, 155, 187, 172]
heights = input(" Enter a list of heights: ").split(",")
student_heights = int(0)
students = int(0)
for height in heights:
    student_heights += int(height.strip())
    students += 1
average_total = round(student_heights / students)
print("The average number for Student heights = ", average_total)
