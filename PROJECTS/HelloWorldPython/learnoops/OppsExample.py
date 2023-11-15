from oopsUtil import Student

# create an object

student = Student('navateja', 'njit', 'datascience', [19,20,18])
print(student)

print(student.calculate_total())
print(student.display_marks())
print(student.display_average())

student2 = Student('Bhanu', 'kmec', 'ml', [19,19,18])
print(student2)
print(student2.calculate_total())
print(student2.display_marks())
print(student2.display_average())