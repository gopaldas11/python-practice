#lets try to drag the maximum value from the list using the for loop.
#marks = input("Enter the Student marks : ").split()
# highest = [int(m) for m in marks]
# for hig in marks:
#     if marks > highest:
#         highest = marks
# print("The highest mark is :", highest)
total = 0
for number in range (2, 101, 2):
        total += number
total += 1
print(total)
total2 = 0
for number in range (1, 101):
        if total2 % 2 == 0:
                total2 += number
print(total)