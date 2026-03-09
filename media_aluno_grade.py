# Student Grade Calculator - Weighted Average
name = input('Student Name: ')
grade1 = float(input('First Grade: '))
weight1 = float(input('First Weight: '))
grade2 = float(input('Second Grade: '))
weight2 = float(input('Second Weight: '))

total_weight = weight1 + weight2
average = ((grade1 * weight1) + (grade2 * weight2)) / total_weight

print(f'\nStudent: {name}')
status = "Approved" if average >= 5 else "Failed"
print(f'Final Grade: {average:.2f} - Status: [{status}]')
